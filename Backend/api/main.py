import joblib
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware  # <-- CORS middleware

app = FastAPI()

# Load model (ensure package_model.pkl same folder me hai)
model = joblib.load("package_model.pkl")  

# Enable CORS for Flutter Web / testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # For testing, all origins allow. Production me specify karo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input schema
class InputData(BaseModel):
    cgpa: float

# Prediction endpoint
@app.post("/predict")
def predict(data: InputData):
    pred = model.predict([[data.cgpa]]) 
    return {"predicted_package": float(pred[0])}
 