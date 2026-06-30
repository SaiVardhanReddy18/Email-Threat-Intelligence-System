import pickle

# Load trained model
with open("models/phishing_detector.pkl", "rb") as f:
    model = pickle.load(f)

# Load TF-IDF vectorizer
with open("models/tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Test email text
email_text = "Your account has been compromised. Click here to reset your password."

# Convert email text to vector
email_vector = vectorizer.transform([email_text])

# Predict
prediction = model.predict(email_vector)

# Output result
if prediction[0] == 1:
    print(" Phishing Email Detected")
else:
    print(" Legitimate Email")
