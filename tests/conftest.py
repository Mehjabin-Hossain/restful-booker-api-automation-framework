import pytest

from api.auth_api import AuthAPI
from api.booking_api import BookingAPI
from utils.config import PASSWORD, USERNAME


@pytest.fixture(scope="session")
def booking_api():
    return BookingAPI()


@pytest.fixture(scope="session")
def auth_api():
    return AuthAPI()


@pytest.fixture(scope="session")
def auth_token(auth_api):
    return auth_api.get_token(USERNAME, PASSWORD)
