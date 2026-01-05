from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from datetime import datetime

# Create FastAPI app
app = FastAPI()

# Serve frontend folder
app.mount("/Front_end", StaticFiles(directory="Front_end"), name="Front_end")

@app.get("/api/hello")
def hello_api():
    return {"message": "Hello from FastAPI!"}

@app.get("/", response_class=HTMLResponse)
def serve_home():
    with open("Front_end/index.html") as f:
        return f.read()
    
@app.get("/api/time")
def get_time():
    return{"server_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}