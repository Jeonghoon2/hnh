from fastapi import FastAPI
from typing import Union
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request
import random

app = FastAPI()

ans = ["This is Hot-🐶", "This is not Hot-🐶"]

html = Jinja2Templates(directory="public")


@app.post("/uploadfile")
async def upload_file(file):

    img = await file.read()
    model = pipeline


@app.get("/predict")
def predict():
    model = pipline("image-classification", model="julien-c/hotdog-not-hotdog")
    return {"message": random.choice(ans)}
