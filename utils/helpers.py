import json


def load_json_data(filename: str) -> list:
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)


def validate_status_code(response, expected_status: int) -> None:
    assert response.status_code == expected_status, (
        f"Expected status code {expected_status}, got {response.status_code}. Response: {response.text}"
    )


def validate_booking_response(booking_json: dict, expected: dict) -> None:
    assert booking_json["firstname"] == expected["firstname"], "Firstname does not match"
    assert booking_json["lastname"] == expected["lastname"], "Lastname does not match"
    assert booking_json["totalprice"] == expected["totalprice"], "Total price does not match"
    assert booking_json["depositpaid"] == expected["depositpaid"], "Deposit paid flag does not match"
    assert booking_json["bookingdates"] == expected["bookingdates"], "Booking dates do not match"
    if "additionalneeds" in expected:
        assert booking_json.get("additionalneeds") == expected.get("additionalneeds"), "Additional needs do not match"
