<<<<<<< HEAD
# Scamnet.ai
AI-powered browser extension that detects scam and phishing messages using NLP.
=======
# SCAMNET-AI
An AI-powered scam detection system that analyzes suspicious messages and warns users before they interact with them.

## Setup Instructions

### 1. Install Dependencies
Ensure you have Python installed, then create the environment and install dependencies:
```bash
python -m venv env
# On Windows:
env\Scripts\activate
# On Mac/Linux:
source env/bin/activate

pip install -r requirements.txt
```

### 2. Train the Model
Run the training script to generate the ML model and vectorizer:
```bash
python train.py
```
This will create `model.pkl` and `vectorizer.pkl`.

### 3. Run the Backend API
Start the FastAPI server:
```bash
uvicorn predict:app --reload
```
The API will be available at http://localhost:8000. You can test the endpoint at http://localhost:8000/docs.

### 4. Install the Browser Extension
1. Open Chrome/Edge and go to `chrome://extensions` or `edge://extensions`.
2. Enable **Developer mode**.
3. Click **Load unpacked** and select the `browser_extension` folder in this project.
4. Pin the extension to your toolbar, click it, and try pasting a message!

## Future Improvements
- More advanced NLP preprocessing
- Transformer models (BERT)
- URL scanning
>>>>>>> be7d022 (Added working extension and ML model)
[Here's the command to run the backend: venv\Scripts\uvicorn predict:app --reload
]
