from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import ScamDetectorModel

app = FastAPI(title="SCAMNET-AI Backend")

# Allow CORS for browser extension
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (including chrome-extension://)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Initialize the model globally
detector = ScamDetectorModel()

class MessageRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "SCAMNET-AI API is running. Use POST /predict to analyze messages."}

@app.post("/predict")
def predict_message(request: MessageRequest):
    result = detector.predict(request.message)
    return result
