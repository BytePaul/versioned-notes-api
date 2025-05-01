from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_note():
    response = client.post("/notes/", json={
        "title": "Test Note",
        "content": "Initial content",
        "tag": "test"
    })
    assert response.status_code == 200
    assert response.json()["version"] == 1
