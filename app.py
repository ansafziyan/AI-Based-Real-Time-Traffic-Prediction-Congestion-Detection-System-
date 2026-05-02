from fastapi import FastAPI
import numpy as np

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Backend Running"}

@app.post("/predict")
def predict(data: dict):
    x = np.array(data["input"], dtype=float)
    prediction = float(np.mean(x) * 10)
    return {"prediction": prediction}
