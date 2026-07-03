# 🛡️ Email Threat Intelligence System (ETIS)

### Machine Learning-Based Phishing Email Detection and Threat Analysis Platform

Email Threat Intelligence System (ETIS) is an intelligent cybersecurity application that combines **Machine Learning** with **real-time threat intelligence** to identify phishing emails through advanced email analysis. The system enhances phishing detection by integrating multiple security techniques, including **VirusTotal API**, **URL reputation analysis**, **sender spoof detection**, **domain similarity detection**, **brand impersonation detection**, **attachment risk analysis**, and **keyword-based threat scoring**.

Unlike traditional phishing detection systems that rely only on machine learning predictions, ETIS performs multiple layers of security analysis to improve detection accuracy and provide meaningful threat insights. The application features an interactive dashboard displaying phishing probability, confidence score, threat score, risk level, URL analysis, VirusTotal detection results, scan history, and downloadable PDF security reports.

This project demonstrates the practical application of **Machine Learning**, **Cybersecurity**, **Threat Intelligence**, **Natural Language Processing (NLP)**, and **Web Application Development**, making it suitable for academic research, cybersecurity learning, and professional portfolio demonstration.

---

## 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Project Highlights](#-project-highlights)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Application Workflow](#-application-workflow)
- [Screenshots](#-screenshots)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

# 📖 Project Overview

Email Threat Intelligence System (ETIS) is a Machine Learning-powered phishing email detection platform designed to identify malicious emails using multiple layers of cybersecurity analysis.

The application combines Artificial Intelligence with real-world threat intelligence to detect phishing attacks more accurately than traditional machine learning models alone. It analyzes email content, sender information, URLs, attachments, and domain similarity before calculating an overall threat score.

ETIS provides users with a comprehensive security report that includes phishing probability, confidence score, URL reputation analysis using VirusTotal, sender verification results, threat score visualization, risk classification, and downloadable PDF reports.

The project has been developed using **Python**, **Flask**, **Scikit-learn**, **TF-IDF Vectorization**, **Chart.js**, and the **VirusTotal API** to demonstrate how Machine Learning can be integrated with practical cybersecurity techniques for phishing detection.

---

# 🚀 Project Highlights

- 🤖 Machine Learning-Based Email Classification
- 🛡️ Real-Time VirusTotal API Integration
- 🔗 URL Threat Detection and Reputation Analysis
- 📧 Sender Spoof Detection
- 🌐 Domain Similarity Detection using Levenshtein Distance
- 🏦 Brand Impersonation Detection
- 📎 Attachment Risk Analysis
- 📊 Interactive Threat Dashboard
- 📈 Threat Score Visualization
- 📄 Downloadable PDF Security Reports
- 📚 Scan History Management
- 🌍 Responsive Web Interface

---

# ✨ Features

- Machine Learning-based phishing email detection
- Real-time VirusTotal API integration
- URL extraction and reputation analysis
- Detection of suspicious shortened URLs
- Sender spoof detection
- Domain similarity detection using Levenshtein Distance
- Brand impersonation detection
- Attachment risk scanner
- Keyword-based phishing detection
- Confidence score calculation
- Dynamic threat score generation
- Risk level classification (Low, Medium, High)
- Interactive security dashboard
- Threat visualization using charts
- Upload and analyze `.txt` email files
- Downloadable PDF security reports
- Recent scan history tracking
- User-friendly Flask web interface

---

# 💻 Tech Stack

## Programming Language

- Python

## Backend Framework

- Flask

## Machine Learning

- Scikit-learn
- TF-IDF Vectorizer

## Frontend

- HTML5
- CSS3
- JavaScript
- Chart.js

## Libraries

- NumPy
- Pandas
- Requests
- ReportLab
- Python-Levenshtein
- python-dotenv

## Threat Intelligence

- VirusTotal API



---

# 📁 Project Structure

```text
Email-Threat-Intelligence-System/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── data/
│   ├── phishing_emails.csv
│   └── preprocessed_data.pkl
│
├── models/
│   ├── phishing_detector.pkl
│   └── tfidf_vectorizer.pkl
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   └── predict.py
│
└── templates/
    └── index.html
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/SaiVardhanReddy18/Email-Threat-Intelligence-System.git
cd Email-Threat-Intelligence-System
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

Install all the required Python libraries.

```bash
pip install -r requirements.txt
```

---

# ⚙️ Configuration

Create a `.env` file in the project root directory.

```env
VT_API_KEY=YOUR_VIRUSTOTAL_API_KEY
```

Replace `YOUR_VIRUSTOTAL_API_KEY` with your own VirusTotal API key.

> **Important:** Never upload your `.env` file to GitHub. The project is already configured to ignore it using `.gitignore`.

---

# 🚀 Usage

## Start the Flask Application

Run:

```bash
python app.py
```

Once the server starts successfully, open your browser and visit:

```
http://127.0.0.1:5000
```

---

## How to Use the Application

1. Enter the sender's email address.
2. Paste the email content into the text area **or** upload a `.txt` email file.
3. Click **Analyze Email**.
4. The system will perform multiple layers of security analysis.
5. Review the generated security report.

The report includes:

- Machine Learning Prediction
- Confidence Score
- Threat Score
- Risk Level
- URL Reputation Analysis
- VirusTotal Detection Results
- Sender Spoof Detection
- Domain Similarity Detection
- Brand Impersonation Detection
- Attachment Risk Analysis
- Scan History
- Downloadable PDF Security Report

---

## Sample Email Analysis Workflow

```
Enter Email
      │
      ▼
Click Analyze Email
      │
      ▼
Machine Learning Prediction
      │
      ▼
Threat Intelligence Analysis
      │
      ▼
Interactive Dashboard
      │
      ▼
Download Security Report
```



---

# 🔍 How It Works

The Email Threat Intelligence System (ETIS) follows a multi-layered security approach to accurately detect phishing emails. Instead of relying solely on Machine Learning predictions, the application combines Artificial Intelligence with Threat Intelligence and rule-based security analysis to improve detection accuracy.

The workflow consists of the following stages:

### 1. Email Input

Users can either:

- Paste email content directly into the application.
- Upload a `.txt` email file for analysis.

The sender's email address is also collected for additional security verification.

---

### 2. Machine Learning Classification

The email content is converted into numerical feature vectors using **TF-IDF Vectorization**.

The trained Machine Learning model analyzes these features and predicts whether the email is:

- Legitimate
- Phishing

A confidence score is generated for every prediction.

---

### 3. Keyword Analysis

The application scans the email for phishing-related keywords such as:

- Verify
- Urgent
- Reset Password
- Account Suspended
- Payment Failed
- Security Alert

Legitimate business keywords are also analyzed to improve prediction accuracy.

---

### 4. URL Extraction & Analysis

All URLs present in the email are automatically extracted.

The application checks for suspicious characteristics including:

- URL Shorteners (Bit.ly, TinyURL)
- Login URLs
- Secure URLs
- Verification URLs
- IP-based URLs

---

### 5. VirusTotal Integration

Each extracted URL is submitted to the VirusTotal API for reputation analysis.

VirusTotal checks the URL against multiple security vendors and returns:

- Malicious detections
- Suspicious detections
- Clean reputation

The detection results contribute to the overall threat score.

---

### 6. Sender Spoof Detection

The sender's email domain is analyzed to detect possible spoofing attempts.

Example:

```
support@paypaI.com
```

instead of

```
support@paypal.com
```

The system identifies suspicious sender domains that attempt to impersonate trusted organizations.

---

### 7. Domain Similarity Detection

The application compares sender domains against trusted domains using **Levenshtein Distance**.

This helps identify look-alike domains commonly used in phishing attacks.

Example:

```
paypaI.com
paypal.com
```

---

### 8. Attachment Risk Analysis

The application scans uploaded email content for risky attachment types including:

- .exe
- .scr
- .zip
- .docm
- .xlsm
- .js

Potentially dangerous attachments increase the overall threat score.

---

### 9. Brand Impersonation Detection

The system detects attempts to impersonate trusted organizations such as:

- Google
- Microsoft
- Amazon
- PayPal
- Apple
- Banks

---

### 10. Threat Score Calculation

The final security score is calculated by combining:

- Machine Learning Prediction
- VirusTotal Results
- URL Risk Analysis
- Sender Spoof Detection
- Domain Similarity
- Attachment Analysis
- Brand Impersonation

The application then classifies the email as:

- 🟢 Low Risk
- 🟡 Medium Risk
- 🔴 High Risk

---

### 11. Interactive Dashboard

The results are presented through an interactive dashboard containing:

- Prediction Result
- Confidence Score
- Threat Score
- Risk Level
- VirusTotal Results
- URL Analysis
- Scan History
- Threat Visualization Charts

---

### 12. PDF Report Generation

Users can download a comprehensive PDF report containing:

- Email Classification
- Threat Score
- Confidence Score
- VirusTotal Results
- Security Findings
- Risk Level
- Analysis Summary

---

# 🔄 Application Workflow

```text
                    Email Input
                         │
                         ▼
              Machine Learning Prediction
                         │
                         ▼
                Keyword-Based Analysis
                         │
                         ▼
                  URL Extraction
                         │
                         ▼
             VirusTotal URL Reputation
                         │
                         ▼
              Sender Spoof Detection
                         │
                         ▼
           Domain Similarity Detection
                         │
                         ▼
             Attachment Risk Analysis
                         │
                         ▼
          Brand Impersonation Detection
                         │
                         ▼
            Threat Score Calculation
                         │
                         ▼
            Interactive Dashboard
                         │
                         ▼
             PDF Report Generation
```

---

# 📸 Screenshots

> Screenshots will be added after deployment.

### 🏠 Home Page

_Add application home page screenshot here._

---

### 📊 Threat Dashboard

_Add dashboard screenshot here._

---

### 🌐 URL Reputation Analysis

_Add VirusTotal analysis screenshot here._

---

### 📄 PDF Security Report

_Add PDF report screenshot here._

---

# 🚀 Future Enhancements

The following features are planned for future releases:

- Gmail API Integration
- Microsoft Outlook Integration
- Docker Deployment
- User Authentication
- Database Storage
- QR Code Phishing Detection
- Malware Attachment Scanning
- Real-Time Email Monitoring
- AI-powered Threat Intelligence
- REST API Support
- Multi-language Support
- Cloud Deployment


---

# 🤝 Contributing

Contributions are welcome and appreciated.

If you would like to improve this project, follow these steps:

1. Fork this repository.
2. Create a new feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push the branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

Please ensure your code follows the project's coding standards and includes clear documentation where applicable.

---

# 📄 License

This project is licensed under the **MIT License**.

See the **LICENSE** file for more information.

---

# 👨‍💻 Author

## Sai Vardhan

**MCA Student | Cybersecurity Enthusiast | Python Developer | Machine Learning Learner**

### Connect with Me

- **GitHub:** https://github.com/SaiVardhanReddy18
- **Email:** saivardhanreddy.2802@gmail.com

---

# 🙏 Acknowledgements

Special thanks to the following technologies and communities that made this project possible:

- Python
- Flask
- Scikit-learn
- VirusTotal API
- Chart.js
- ReportLab
- Open Source Community

---

# ⭐ Support

If you found this project useful:

⭐ Star this repository

🍴 Fork this repository

📢 Share it with others

Your support is greatly appreciated!

---

# ⚠️ Disclaimer

This project has been developed for **educational, research, and cybersecurity learning purposes only**.

The VirusTotal API is used in accordance with its public API terms of service.

Users are responsible for complying with all applicable laws and organizational policies when using this software.

---

# 🎯 Project Status

**Current Version:** v1.0

### Implemented Features

- ✅ Machine Learning Email Classification
- ✅ VirusTotal API Integration
- ✅ URL Reputation Analysis
- ✅ Sender Spoof Detection
- ✅ Domain Similarity Detection
- ✅ Attachment Risk Analysis
- ✅ Brand Impersonation Detection
- ✅ Threat Score Dashboard
- ✅ PDF Report Generation
- ✅ Scan History

### Planned Features

- 🔄 Gmail API Integration
- 🔄 Outlook Integration
- 🔄 Docker Deployment
- 🔄 User Authentication
- 🔄 Database Support
- 🔄 Cloud Deployment

---

## 💙 Thank You

Thank you for visiting this repository.

If you have any suggestions, improvements, or feedback, feel free to open an issue or submit a pull request.

Happy Coding! 🚀