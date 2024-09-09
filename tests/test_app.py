import pytest
from app.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    response = client.get('/')
    assert response.data == b'Hello, World!'
    assert response.status_code == 200

def test_about(client):
    response = client.get('/about')
    assert response.data == b'About this app'
    assert response.status_code == 200

def test_add(client):
    response = client.get('/add/2/3')
    assert response.data == b'5'
    assert response.status_code == 200
