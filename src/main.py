import asyncio
from fastapi import FastAPI
import time
import random

app = FastAPI()

@app.get("/text")
async def get_text():
    return {"message": "Large text"}

@app.get("/compute")
async def compute():
    start_time = time.time()
    result = sum(i ** 2 for i in range(5000000))  # Long measuring
    elapsed_time = time.time() - start_time
    return {"result": result, "time": elapsed_time}

@app.get("/sleep")
async def sleep_api():
    sleep_time = random.uniform(1, 3)
    await asyncio.sleep(sleep_time)
    return {"message": "Load...", "sleep_time": sleep_time}
