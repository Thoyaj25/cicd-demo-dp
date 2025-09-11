import pytest
from myapp import app  # updated import

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello World!" in response.data

def test_basic_math():
    assert 1 + 1 == 2
