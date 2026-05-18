import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


data = {
    "review": [
        "good product", "very bad product", "excellent service",
        "not good", "amazing experience", "poor quality",
        "happy with service", "worst experience",
        "nice product", "very disappointing"
    ],
    "sentiment": [
        "positive", "negative", "positive",
        "negative", "positive", "negative",
        "positive", "negative", "positive", "negative"
    ]
}

df = pd.DataFrame(data)


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

df["cleaned_review"] = df["review"].apply(clean_text)


vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["cleaned_review"])
y = df["sentiment"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)


model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)


print("Accuracy:", accuracy_score(y_test, y_pred))


test_text = ["this product is good"]

test_clean = [clean_text(test_text[0])]
test_vector = vectorizer.transform(test_clean)

prediction = model.predict(test_vector)

print("\nReview:", test_text[0])
print("Predicted Sentiment:", prediction[0])