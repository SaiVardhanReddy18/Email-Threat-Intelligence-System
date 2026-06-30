import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load dataset
data = pd.read_csv("phishing_emails.csv")

X = data["text"]
y = data["label"]

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1, 2)
)

X_tfidf = vectorizer.fit_transform(X)

# Save vectorizer
with open("models/tfidf_vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

# Save processed data
with open("data/preprocessed_data.pkl", "wb") as f:
    pickle.dump((X_tfidf, y), f)

print(" Preprocessing completed successfully")
