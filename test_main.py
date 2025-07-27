import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI app!"}

@pytest.mark.asyncio
async def test_say_hello():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/hello", params={"name": "Alice"})
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Alice!"}

@pytest.mark.asyncio
async def test_say_hello_missing_name():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/hello")
    assert response.status_code == 422  # Unprocessable Entity for missing required query param 