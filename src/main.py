import asyncio
import uuid

from fastapi import FastAPI
import time
import random
from locust import HttpUser, task, between
from tinydb import TinyDB, Query

from src.db.chroma_manager import collection
from src.services.ollama_service import make_ollama_request, make_ollama_request_with_vectors
from src.services.sys_diagnostics import get_system_info
from src.db.base import create_diagnostics, get_diagnostics

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


@app.post("/metrix/chroma/vectors")
async def convert_metrix_to_vectors():
    res = get_diagnostics(6)
    pairs = [res[i:i + 2] for i in range(0, len(res), 2)]
    for pair in pairs:
        llm_res = make_ollama_request(pair)
        print(llm_res)
        collection.add(
            documents=[
                llm_res
            ],
            ids=[str(uuid.uuid4())],
        )
    return res


@app.get("/metrix/chroma/list")
async def get_llm_query():
    results = collection.get()
    return results


@app.get("/metrix/llm_query")
async def get_llm_query():
    results = collection.query(
        query_texts=["Best recommendation to improve system performance"],  # Chroma will embed this for you
        n_results=1  # how many results to return
    )
    llm_res = make_ollama_request_with_vectors(results['documents'][0])

    return llm_res


@app.get("/metrix/{times}")
async def collect_metrix(times: int = 10):
    counter = 0
    while counter < times:
        metrics_data = get_system_info()
        create_diagnostics(metrics_data)
        counter += 1
        await asyncio.sleep(1)
