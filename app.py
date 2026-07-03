from flask import Flask, render_template, request, send_file
import pickle
import re
import Levenshtein
from datetime import datetime
import requests
import base64
import os
from dotenv import load_dotenv

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

load_dotenv()

app = Flask(__name__)
VT_API_KEY = os.getenv("VT_API_KEY")


latest_report = {}
scan_history = []




PHISHING_KEYWORDS = [
    "suspended", "terminated", "locked", "compromised",
    "verify", "urgent", "immediately", "reset password",
    "security alert", "unauthorized", "click here",
    "payment failed", "account blocked", "otp", "bank"
]

LEGITIMATE_KEYWORDS = [
    "meeting", "schedule", "agenda", "project",
    "report", "attached", "invoice", "delivered",
    "confirmation", "class", "assignment", "timetable",
    "no action required", "thank you"
]



def keyword_score(email_text):
    email_text = email_text.lower()

    phishing_score = sum(
        1 for word in PHISHING_KEYWORDS if word in email_text
    )

    legitimate_score = sum(
        1 for word in LEGITIMATE_KEYWORDS if word in email_text
    )

    return phishing_score, legitimate_score



def url_risk_analyzer(email_text):
    
    suspicious_score = 0

    urls = re.findall(r'https?://\S+', email_text)

    suspicious_words = [
        "verify",
        "secure",
        "login",
        "update",
        "bank",
        "account"
    ]

    for url in urls:

        if re.search(r'bit\.ly|tinyurl|goo\.gl', url):
            suspicious_score += 20

        if re.search(r'http://\d+\.\d+\.\d+\.\d+', url):
            suspicious_score += 25

        for word in suspicious_words:
            if word in url.lower():
                suspicious_score += 15

    return suspicious_score


def attachment_risk_scanner(email_text):

    risky_extensions = [
        ".exe",
        ".zip",
        ".scr",
        ".js",
        ".docm",
        ".xlsm"
    ]

    score = 0

    for ext in risky_extensions:
        if ext in email_text.lower():
            score += 2

    return score



def fake_domain_detector(sender_email):

    trusted_domains = [
        "paypal.com",
        "amazon.com",
        "google.com",
        "microsoft.com"
    ]

    if "@" not in sender_email:
        return False

    domain = sender_email.split("@")[1].lower()

    for trusted in trusted_domains:

        similarity = Levenshtein.distance(domain, trusted)

        if similarity <= 2 and domain != trusted:
            return True

    return False



def sender_spoof_detector(sender_email):

    suspicious_keywords = [
        "paypal",
        "amazon",
        "google",
        "microsoft",
        "apple",
        "bank",
        "secure",
        "verify",
        "login",
        "support",
        "alert"
    ]

    if "@" not in sender_email:
        return False

    domain = sender_email.split("@")[1].lower()

    trusted_domains = [
        "paypal.com",
        "amazon.com",
        "google.com",
        "microsoft.com",
        "apple.com"
    ]

    if domain in trusted_domains:
        return False

    for keyword in suspicious_keywords:
        if keyword in domain:
            return True

    return False


def brand_impersonation_detector(email_text, sender_email):

    brands = [
        "paypal",
        "amazon",
        "google",
        "microsoft",
        "apple",
        "bank"
    ]

    email_text = email_text.lower()
    sender_email = sender_email.lower()

    for brand in brands:

        if brand in email_text and brand not in sender_email:
            return True

    return False

def check_url_virustotal(url):
    
    try:

        headers = {
            "x-apikey": VT_API_KEY
        }

        response = requests.post(
            "https://www.virustotal.com/api/v3/urls",
            headers=headers,
            data={"url": url}
        )

        print("Checking URL:", url)
        print("VirusTotal Status:", response.status_code)

        if response.status_code == 200:

            analysis_id = response.json()["data"]["id"]

            analysis_response = requests.get(
                f"https://www.virustotal.com/api/v3/analyses/{analysis_id}",
                headers=headers
            )

            if analysis_response.status_code == 200:

                stats = analysis_response.json()[
                    "data"
                ]["attributes"]["stats"]

                return stats["malicious"]

    except Exception as e:
        print("VirusTotal Error:", e)

    return 0

def threat_score_dashboard(
    url_score,
    attachment_score,
    spoof_flag,
    similarity_flag
):

    total_score = 0
    reasons = []

    if url_score > 0:
        total_score += 25
        reasons.append("Suspicious URL detected")

    if attachment_score > 0:
        total_score += 20
        reasons.append("Dangerous attachment detected")

    if spoof_flag:
        total_score += 25
        reasons.append("Sender spoofing detected")

    if similarity_flag:
        total_score += 25
        reasons.append("Lookalike domain detected")

    return min(total_score, 100), reasons


with open("models/phishing_detector.pkl", "rb") as f:
    model = pickle.load(f)

with open("models/tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


@app.route("/", methods=["GET", "POST"])
def home():

    global latest_report

    result = ""
    confidence = 0
    risk = "LOW"
    security_score = 0
    reasons = []

    phish_prob = 0
    legit_prob = 0

    urls = []
    suspicious_url_count = 0
    vt_score = 0
    url_results = []
    total_urls = 0
    safe_urls = 0

    if request.method == "POST":

        email_text = request.form.get("email", "")
        sender_email = request.form.get("sender", "")

        uploaded_file = request.files.get("email_file")

        if uploaded_file and uploaded_file.filename != "":
            try:
                email_text = uploaded_file.read().decode("utf-8")
            except:
                email_text = ""

        if not email_text.strip():

            return render_template(
                "index.html",
                message="Please enter email content or upload a .txt file.",
                result="",
                confidence=0,
                risk="LOW",
                security_score=0,
                reasons=[],
                phish_prob=0,
                legit_prob=0,
                urls=[],
                suspicious_url_count=0,
                total_urls=0,
                safe_urls=0,
                vt_score=0,
                scan_history=scan_history
            )

        # ML Prediction
        email_vector = vectorizer.transform([email_text])

        prediction = model.predict(email_vector)

        probability = model.predict_proba(email_vector)[0]

        phish_prob = probability[1] * 100
        legit_prob = probability[0] * 100

        # Keyword Analysis
        phish_score, legit_score = keyword_score(email_text)

        # URL Extraction
        urls = re.findall(r'https?://\S+', email_text)

        total_urls = len(urls)

        # URL Risk Analysis
                # URL Extraction
        urls = re.findall(r'https?://\S+', email_text)

        total_urls = len(urls)

        # URL Risk Analysis
        url_score = url_risk_analyzer(email_text)

        url_results = []

        for url in urls:

            print("FOUND URL:", url)

            status = "Safe"

            if (
                "bit.ly" in url.lower()
                or "tinyurl" in url.lower()
                or "verify" in url.lower()
                or "secure" in url.lower()
            ):
                suspicious_url_count += 1
                status = "Suspicious"

            vt_hits = check_url_virustotal(url)
            print("VT HITS =", vt_hits)
            vt_score += vt_hits

            url_results.append({
                "url": url,
                "status": status,
                "vt_hits": vt_hits
            })

        safe_urls = total_urls - suspicious_url_count

            

               # Other Security Checks
        attachment_score = attachment_risk_scanner(email_text)

        spoof_flag = sender_spoof_detector(sender_email)

        similarity_flag = fake_domain_detector(sender_email)

        brand_flag = brand_impersonation_detector(
            email_text,
            sender_email
        )

        security_score, reasons = threat_score_dashboard(
            url_score,
            attachment_score,
            spoof_flag,
            similarity_flag
        )

        if brand_flag:
            security_score += 20
            reasons.append("Brand impersonation detected")

        if vt_score > 0:
            security_score += 25
            reasons.append(
                f"VirusTotal flagged URL ({vt_score} detections)"
            )

        # Classification Logic
        if phish_score > legit_score:

            result = "Phishing Email Detected"
            confidence = round(phish_prob, 2)

        elif legit_score > phish_score:

            result = "Legitimate Email"
            confidence = round(legit_prob, 2)

        else:

            if prediction[0] == 1:

                result = "Phishing Email Detected"
                confidence = round(phish_prob, 2)

            else:

                result = "Legitimate Email"
                confidence = round(legit_prob, 2)

        # Final Risk Logic

    if result == "Legitimate Email":

        risk = "LOW"

    else:

        if security_score >= 75:
            risk = "HIGH"

        elif security_score >= 40:
            risk = "MEDIUM"

        else:
            risk = "LOW"


    # Save Report
    latest_report = {
        "result": result,
        "confidence": confidence,
        "risk": risk,
        "security_score": security_score,
        "reasons": reasons,
        "urls": urls
    }

    # Scan History
    if result:

        scan_history.insert(0, {
            "result": result,
            "risk": risk,
            "time": datetime.now().strftime(
                "%d-%b-%Y %I:%M:%S %p"
            )
        })

        scan_history[:] = scan_history[:10]

    return render_template(
        "index.html",
        result=result,
        confidence=confidence,
        risk=risk,
        security_score=security_score,
        reasons=reasons,
        phish_prob=round(phish_prob, 2),
        legit_prob=round(legit_prob, 2),
        urls=urls,
        url_results=url_results,
        suspicious_url_count=suspicious_url_count,
        total_urls=total_urls,
        safe_urls=safe_urls,
        vt_score=vt_score,
        scan_history=scan_history
    )



@app.route("/download-report")
def download_report():

    pdf_file = "PhishGuard_Report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph("PhishGuard AI Security Report", styles["Title"])
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"Result: {latest_report.get('result', 'N/A')}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Confidence: {latest_report.get('confidence', 0)}%",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Threat Score: {latest_report.get('security_score', 0)}%",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Risk Level: {latest_report.get('risk', 'N/A')}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph("Threat Analysis:", styles["Heading2"])
    )

    for reason in latest_report.get("reasons", []):

        content.append(
            Paragraph(f"• {reason}", styles["Normal"])
        )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph("Detected URLs:", styles["Heading2"])
    )

    for url in latest_report.get("urls", []):

        content.append(
            Paragraph(url, styles["Normal"])
        )

    doc.build(content)

    return send_file(
        pdf_file,
        as_attachment=True
    )




if __name__ == "__main__":
    app.run(debug=True)