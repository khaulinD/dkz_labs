import asyncio

from fastapi import FastAPI
import time
import random
from locust import HttpUser, task, between
from tinydb import TinyDB, Query

# Ініціалізація бази даних TinyDB
db = TinyDB("api_requests.json")

app = FastAPI()

@app.get("/text")
async def get_text():
    start_time = time.time()
    response = {"message": "Це текстові дані"}
    elapsed_time = time.time() - start_time
    db.insert({"endpoint": "/text", "response_time": elapsed_time})
    return response

@app.get("/compute")
async def compute():
    start_time = time.time()
    result = sum(i ** 2 for i in range(5000000))  # Довге обчислення
    elapsed_time = time.time() - start_time
    db.insert({"endpoint": "/compute", "response_time": elapsed_time})
    return {"result": result, "time": elapsed_time}

@app.get("/sleep")
async def sleep_api():
    sleep_time = random.uniform(1, 3)
    await asyncio.sleep(sleep_time)
    start_time = time.time()
    response = {"message": "Очікування завершене", "sleep_time": sleep_time}
    elapsed_time = time.time() - start_time
    db.insert({"endpoint": "/sleep", "response_time": elapsed_time})
    return response
