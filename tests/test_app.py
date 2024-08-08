from http import HTTPStatus


def test_should_be_return_status_ok_and_hello_world(client):
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Hello, world!"}
