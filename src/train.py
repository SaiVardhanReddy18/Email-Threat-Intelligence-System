import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data
with open("data/preprocessed_data.pkl", "rb") as f:
    X, y = pickle.load(f)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model (BEST FOR TEXT)
model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced"
)

model.fit(X_train, y_train)

# Test
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))

# Save model
with open("models/phishing_detector.pkl", "wb") as f:
    pickle.dump(model, f)

print(" Model trained and saved successfully")
