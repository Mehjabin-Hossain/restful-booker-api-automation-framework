import requests

from utils.config import BASE_URL, BOOKING_PATH


class BookingAPI:
    def __init__(self, base_url: str = BASE_URL):
        self.booking_url = f"{base_url}{BOOKING_PATH}"

    def get_booking_ids(self) -> requests.Response:
        return requests.get(self.booking_url)

    def get_booking(self, booking_id: int) -> requests.Response:
        return requests.get(f"{self.booking_url}/{booking_id}")

    def create_booking(self, payload: dict) -> requests.Response:
        return requests.post(self.booking_url, json=payload, headers=self.default_headers())

    def update_booking(self, booking_id: int, payload: dict, token: str) -> requests.Response:
        return requests.put(
            f"{self.booking_url}/{booking_id}",
            json=payload,
            headers=self.auth_headers(token),
        )

    def partial_update_booking(self, booking_id: int, payload: dict, token: str) -> requests.Response:
        return requests.patch(
            f"{self.booking_url}/{booking_id}",
            json=payload,
            headers=self.auth_headers(token),
        )

    def delete_booking(self, booking_id: int, token: str) -> requests.Response:
        return requests.delete(
            f"{self.booking_url}/{booking_id}",
            headers=self.auth_headers(token),
        )

    @staticmethod
    def default_headers() -> dict:
        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    @staticmethod
    def auth_headers(token: str) -> dict:
        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Cookie": f"token={token}",
        }
