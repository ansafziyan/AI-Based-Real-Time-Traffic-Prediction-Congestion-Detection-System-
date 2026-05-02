from fastapi import FastAPI
from fastapi.responses import FileResponse
import numpy as np

app = FastAPI()

@app.get("/")
def home():
    return FileResponse("index.html")

@app.post("/predict")
def predict(data: dict):
    x = np.array(data["input"], dtype=float)
    prediction = float(np.mean(x) * 10)
    return {"prediction": prediction}
