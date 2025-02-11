from fastapi import FastAPI, Body
from datetime import datetime

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Service 2 is live!", "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

@app.post("/echo")
def echo(data: dict = Body(...)):
    return {"received_data": data, "confirmation": "Data received successfully!"}
