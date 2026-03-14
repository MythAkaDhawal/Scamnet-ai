# SCAMNET-AI – Baseline Model Setup Guide 🚀

This guide walks through the **initial development steps** for building the first working version of the SCAMNET-AI scam detection system.

The goal of this stage is simple:
Build a **baseline machine learning model** that can detect spam or scam messages using the **SMS Spam Dataset**.

This baseline will later be improved with more advanced techniques such as better NLP preprocessing, phishing URL analysis, and transformer models.

---

# Project Folder Structure 📂

To keep things simple and manageable, the project uses a minimal structure:

```
SCAMNET-AI
│
├── data
│   └── spam.csv
│
├── scam_detector.ipynb
│
├── requirements.txt
└── README.md
```

### Explanation

**data/**
Stores datasets used for training and experimentation.

**spam.csv**
The SMS spam dataset used to train the first model.

**scam_detector.ipynb**
The main notebook where all experiments and model training happen.

**requirements.txt**
Lists Python dependencies required to run the project.

**README.md**
Overview of the project.

---

# Step 1 — Create the Project Folder

Create a new folder for the project.

```
SCAMNET-AI
```

Inside the folder create:

```
data
```

Place the downloaded dataset inside this folder.

---

# Step 2 — Create a Virtual Environment ⚙️

Open a terminal inside the project folder.

Create a virtual environment:

```
python -m venv venv
```

Activate it:

### Windows

```
venv\Scripts\activate
```

Using a virtual environment keeps project dependencies isolated.

---

# Step 3 — Install Required Libraries 📦

Create a file called:

```
requirements.txt
```

Add the following:

```
pandas
numpy
scikit-learn
matplotlib
seaborn
nltk
jupyter
```

Install the dependencies:

```
pip install -r requirements.txt
```

---

# Step 4 — Download the Dataset 📊

Use the **SMS Spam Collection Dataset**.

This dataset contains **over 5,000 SMS messages**, each labeled as:

```
ham  → normal message
spam → scam or promotional message
```

Rename the file to:

```
spam.csv
```

Place it in:

```
data/spam.csv
```

---

# Step 5 — Create the Notebook

Create a notebook file:

```
scam_detector.ipynb
```

Open it using:

* Jupyter Notebook
* VS Code
* Google Colab

---

# Step 6 — Import Required Libraries

First cell in the notebook:

```python
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
```

These libraries are used for:

* data processing
* feature extraction
* model training
* evaluation

---

# Step 7 — Load the Dataset

Load the dataset into a dataframe.

```python
data = pd.read_csv("data/spam.csv", encoding="latin-1")

data.head()
```

The dataset usually contains extra columns like:

```
v1
v2
Unnamed: 2
Unnamed: 3
```

Only the first two columns are needed.

---

# Step 8 — Clean the Dataset

Remove unnecessary columns.

```python
data = data[['v1', 'v2']]
data.columns = ['label', 'message']

data.head()
```

After cleaning, the dataset should look like:

```
label   message
ham     Hey are we meeting today?
spam    You won a prize! Call now!
```

---

# Step 9 — Convert Labels to Numbers

Machine learning models require numerical labels.

Convert text labels to numeric values.

```python
data['label'] = data['label'].map({
    'ham': 0,
    'spam': 1
})
```

Label meaning:

```
0 → normal message
1 → spam or scam message
```

---

# Step 10 — Convert Text into Numerical Features

Machine learning models cannot understand raw text.

The text must be converted into numeric features using **TF-IDF vectorization**.

```python
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(data['message'])

y = data['label']
```

TF-IDF captures the importance of words based on how often they appear across messages.

---

# Step 11 — Split the Dataset

Split the dataset into **training data and testing data**.

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

Typical split:

```
80% training data
20% testing data
```

Training data is used to train the model, while testing data evaluates performance.

---

# Step 12 — Train the Machine Learning Model

Start with a simple baseline model.

```python
model = LogisticRegression()

model.fit(X_train, y_train)
```

Logistic Regression is commonly used for **text classification problems**.

---

# Step 13 — Evaluate Model Performance

Test the trained model on unseen data.

```python
predictions = model.predict(X_test)

print(classification_report(y_test, predictions))
print("Accuracy:", accuracy_score(y_test, predictions))
```

Typical metrics reported:

```
precision
recall
f1-score
accuracy
```

Most baseline spam detection models achieve **95–98% accuracy** on this dataset.

---

# Step 14 — Test a Custom Message

The model can now predict whether a new message is suspicious.

```python
test_message = ["Your bank account will be suspended. Click this link now!"]

test_vector = vectorizer.transform(test_message)

prediction = model.predict(test_vector)

if prediction[0] == 1:
    print("⚠️ Scam message detected")
else:
    print("✅ Message looks safe")
```

Example output:

```
⚠️ Scam message detected
```

---

# What Has Been Built So Far 🧠

At this stage the project includes:

✔ A working **machine learning scam detection model**
✔ Text feature extraction using TF-IDF
✔ A trained classifier for spam detection
✔ Baseline evaluation metrics

This forms the **foundation for further research and improvements**.

---

# Future Improvements 🚀

The baseline system will later be expanded with:

**Better NLP preprocessing**

* stopword removal
* lemmatization
* text normalization

**More advanced models**

* Random Forest
* Gradient Boosting
* Transformer models (BERT)

**Hybrid scam detection**

* message analysis
* phishing URL detection
* behavioral patterns

**Explainable predictions**

The system will explain *why* a message is flagged as suspicious.

**User interface**

Eventually a simple interface where users can paste a message or link and get a risk score.

---

# Author 👨‍💻

Dhawal Lamba
B.Tech Computer Science (AI & ML)

Curious about AI, cybersecurity, and building experimental systems that solve real-world problems.
