from fastapi import FastAPI
from typing import Union
from fastapi import pi
import random

app = FastAPI()

ans = ["This is Hot-🐶", "This is not Hot-🐶"]


@app.get("/predict")
def predict():
    model = pipline("image-classification", model="julien-c/hotdog-not-hotdog")
    return {"message": random.choice(ans)}
