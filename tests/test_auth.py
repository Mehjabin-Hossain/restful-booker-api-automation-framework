from utils.config import PASSWORD, USERNAME


def test_create_auth_token(auth_api):
    response = auth_api.create_token(USERNAME, PASSWORD)
    assert response.status_code == 200
    assert "token" in response.json()
    assert response.json()["token"] != ""
