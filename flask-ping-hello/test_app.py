import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_ping_returns_pong_and_200(client):
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.data == b'pong'

def test_hello_returns_hello_world_and_200(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.data == b'Hello World'

def test_undefined_route_returns_404(client):
    response = client.get('/undefined')
    assert response.status_code == 404
