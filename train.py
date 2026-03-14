import pandas as pd
import numpy as np
import joblib
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

from model import preprocess_text

print("Loading datasets...")
data1 = pd.read_csv("data/spam.csv", encoding="latin-1")
data2 = pd.read_csv("data/spam2.csv")

# Clean first dataset
data1 = data1[['v1', 'v2']]
data1.columns = ['label', 'message']

# Clean second dataset
data2.columns = ['label', 'message']

# Merge datasets
data = pd.concat([data1, data2]).drop_duplicates().sample(frac=1).reset_index(drop=True)

# Convert labels to numeric (ham=0, spam=1)
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

print("Preprocessing text...")
data['processed_message'] = data['message'].apply(preprocess_text)

# Convert text to features
print("Vectorizing text...")
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['processed_message'])
y = data['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
print("Training model...")
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate model
print("Evaluating model...")
predictions = model.predict(X_test)
print(classification_report(y_test, predictions))
print("Accuracy:", accuracy_score(y_test, predictions))

# Export model and vectorizer
print("Exporting model to disk...")
joblib.dump(model, 'model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("Training finished successfully. model.pkl and vectorizer.pkl saved.")
