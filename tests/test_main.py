from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data


def test_get_gists_octocat():
    response = client.get("/octocat")
    assert response.status_code == 200
    gists = response.json()
    assert isinstance(gists, list)
    assert len(gists) > 0
