from fastapi import FastAPI
import numpy as np

app = FastAPI()

def predict_model(x):
    return float(np.mean(x) * 10)

@app.get("/")
def home():
    return {"message": "AI Backend Running"}

@app.post("/predict")
def predict(data: dict):
    x = np.array(data["input"], dtype=float)
    prediction = predict_model(x)
    return {"prediction": prediction}
