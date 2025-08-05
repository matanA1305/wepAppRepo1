from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!!!!"}

@app.get("/hello")
def say_hello(name: str = Query(..., description="Name to greet")):
    return {"message": f"Hello, {name}!"} 