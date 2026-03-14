import joblib
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Ensure resources are downloaded
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet', quiet=True)

def preprocess_text(text):
    """
    Cleans text by converting to lowercase, removing punctuation, 
    removing stopwords, and lemmatizing the words.
    """
    text = str(text).lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    words = text.split()
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return ' '.join(words)

class ScamDetectorModel:
    def __init__(self, model_path='model.pkl', vectorizer_path='vectorizer.pkl'):
        try:
            self.model = joblib.load(model_path)
            self.vectorizer = joblib.load(vectorizer_path)
            self.is_loaded = True
        except Exception as e:
            print(f"Error loading model: {e}")
            self.is_loaded = False

    def predict(self, message: str) -> dict:
        if not self.is_loaded:
            return {"error": "Model not loaded properly"}

        # Preprocess the message
        processed_message = preprocess_text(message)
        
        # Vectorize
        vectorized_message = self.vectorizer.transform([processed_message])
        
        # Predict probability
        probability = self.model.predict_proba(vectorized_message)[0][1] # Probability of class 1 (spam)
        
        # Predict class
        prediction_class = self.model.predict(vectorized_message)[0]
        prediction_label = "Scam message" if prediction_class == 1 else "Safe"
        
        return {
            "scam_probability": round(probability * 100, 2),
            "prediction": prediction_label
        }
