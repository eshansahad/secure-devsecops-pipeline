from app.app import app

client = app.test_client()


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to Secure DevSecOps Pipeline" in response.data


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.get_json() == {"version": "1.0.0"}