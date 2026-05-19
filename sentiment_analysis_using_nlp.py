from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
url = "https://raw.githubusercontent.com/Ankit152/IMDB-sentiment-analysis/refs/heads/master/IMDB-Dataset.csv"

df = pd.read_csv(url)

X = df["review"]
y = df["sentiment"]

tokenize = TfidfVectorizer(stop_words='english', lowercase=True)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train = tokenize.fit_transform(X_train)
X_test = tokenize.transform(X_test)
y_test = tokenize.transform(y_test)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
accuracy = model.score(y_test, pred)
print(accuracy)

new_review = ["didn't the acting", "liked the acting", "actor was handsome", "waste of time"]
vector_review = tokenize.transform(new_review)
new_sentiment = model.predict(vector_review)
print(new_sentiment)