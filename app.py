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

    # Inputs:
    # [0] Vehicle Count
    # [1] Avg Speed
    # [2] Signal Delay
    # [3] Road Width
    # [4] Time of Day
    # [5] Road Condition
    # [6] Traffic Density
    # [7] Accident Severity

    score = (
        x[0] * 0.2 +             # vehicle count
        (100 - x[1]) * 0.15 +    # lower speed → more traffic
        x[2] * 0.15 +            # signal delay
        (20 - x[3]) * 1.5 +      # narrow road → more traffic
        (10 if 7 <= x[4] <= 10 or 17 <= x[4] <= 21 else 0) +  # rush hour
        (10 - x[5]) * 2 +        # bad road
        x[6] * 5 +               # density
        x[7] * 3                 # accident
    )

    score = max(0, min(score, 100))

    return {"prediction": round(score, 2)}
