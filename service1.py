from fastapi import FastAPI, Query
import random

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Service 1 is running!", "status": random.choice(["active", "idle", "busy"])}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}! Welcome to Service 1."}

@app.get("/square")
def square(number: int = Query(..., description="Provide a number to square")):
    return {"number": number, "square": number ** 2}
