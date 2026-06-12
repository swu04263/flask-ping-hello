import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_ping(client):
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.data.decode() == 'pong'

def test_hello(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.data.decode() == 'Hello World'

def test_404(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404

def test_ping_post(client):
    response = client.post('/ping')
    assert response.status_code == 405  # 方法不允许

def test_hello_post(client):
    response = client.post('/hello')
    assert response.status_code == 405