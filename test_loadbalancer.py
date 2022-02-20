import pytest
from loadbalancer import loadbalancer

@pytest.fixture
def client():
    with loadbalancer.test_client() as client:
        yield client

def test_path_routing_mango(client):
    result = client.get('/mango')
    assert b'This is the mango application.' in result.data


def test_path_routing_apple(client):
    result = client.get('/apple')
    assert b'This is the apple application.' in result.data


def test_path_routing_notfound(client):
    result = client.get('/notmango')
    assert b'Not Found' in result.data
    assert 404 == result.status_code
