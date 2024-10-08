from app.app import app


def test_hello():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'


def test_name():
    response = app.test_client().get('/name/John')
    assert response.status_code == 200
    assert response.data == b'Hello, John!'


def test_age():
    response = app.test_client().get('/age/25')
    assert response.status_code == 200
    assert response.data == b'You are 25 years old.'


def test_404():
    response = app.test_client().get('/nonexistent')
    assert response.status_code == 404
