# app.py
from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Running", "message": "Voice agent is deployed!"}

@app.post("/start-agent")
def start_agent():
    subprocess.Popen(["python", "agent.py"])
    return {"message": "Agent started"}
