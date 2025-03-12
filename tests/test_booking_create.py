import os

from utils.helpers import validate_booking_response, validate_status_code
from utils.payloads import create_booking_payload
from utils.helpers import load_json_data


def test_create_booking(booking_api):
    file_path = os.path.join(os.path.dirname(__file__), "..", "test_data", "booking_data.json")
    booking_data = load_json_data(file_path)[0]

    payload = create_booking_payload(
        firstname=booking_data["firstname"],
        lastname=booking_data["lastname"],
        totalprice=booking_data["totalprice"],
        depositpaid=booking_data["depositpaid"],
        checkin=booking_data["bookingdates"]["checkin"],
        checkout=booking_data["bookingdates"]["checkout"],
        additionalneeds=booking_data.get("additionalneeds", "Breakfast"),
    )

    response = booking_api.create_booking(payload)
    validate_status_code(response, 200)
    response_json = response.json()
    assert "bookingid" in response_json
    assert "booking" in response_json
    validate_booking_response(response_json["booking"], payload)
