import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI app!"}

def test_say_hello():
    response = client.get("/hello", params={"name": "Alice"})
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Alice!"}

def test_say_hello_missing_name():
    response = client.get("/hello")
    assert response.status_code == 422  # Unprocessable Entity for missing required query param 