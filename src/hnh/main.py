from fastapi import FastAPI
import random

app = FastAPI()

ans = ["This is Hot-🐶", "This is not Hot-🐶"]


@app.get("/predict")
def predict():

    return {"message": random.choice(ans)}
