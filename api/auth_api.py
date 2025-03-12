import requests

from utils.config import AUTH_PATH, BASE_URL


class AuthAPI:
    def __init__(self, base_url: str = BASE_URL):
        self.auth_url = f"{base_url}{AUTH_PATH}"

    def create_token(self, username: str, password: str) -> requests.Response:
        """Create a new authentication token."""
        response = requests.post(self.auth_url, json={"username": username, "password": password})
        return response

    def get_token(self, username: str, password: str) -> str:
        """Return the authentication token string for valid credentials."""
        response = self.create_token(username, password)
        response.raise_for_status()
        return response.json().get("token")
