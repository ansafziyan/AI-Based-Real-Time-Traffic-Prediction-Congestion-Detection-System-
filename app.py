from fastapi import FastAPI
import numpy as np
import tensorflow as tf

app = FastAPI()

# ✅ Load locally trained model
model = tf.keras.models.load_model("model.h5")

@app.get("/")
def home():
    return {"message": "AI Backend Running"}

@app.post("/predict")
def predict(data: dict):
    x = np.array(data["input"], dtype=float).reshape(1, -1)
    prediction = model.predict(x).tolist()
    return {"prediction": prediction}