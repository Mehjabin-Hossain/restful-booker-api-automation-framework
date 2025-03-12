from utils.helpers import validate_booking_response, validate_status_code
from utils.payloads import create_booking_payload, update_booking_payload
from utils.config import PASSWORD, USERNAME


def test_update_booking(booking_api, auth_token):
    booking_data = create_booking_payload(
        firstname="Before",
        lastname="Update",
        totalprice=120,
        depositpaid=True,
        checkin="2025-05-01",
        checkout="2025-05-10",
        additionalneeds="Lunch",
    )

    create_response = booking_api.create_booking(booking_data)
    validate_status_code(create_response, 200)
    created = create_response.json()
    booking_id = created["bookingid"]

    updated_data = update_booking_payload(
        booking_data,
        firstname="After",
        lastname="Update",
        totalprice=150,
        depositpaid=False,
        bookingdates={"checkin": "2025-06-01", "checkout": "2025-06-07"},
        additionalneeds="Dinner",
    )

    update_response = booking_api.update_booking(booking_id, updated_data, auth_token)
    validate_status_code(update_response, 200)

    booked = update_response.json()
    validate_booking_response(booked, updated_data)


def test_partial_update_booking(booking_api, auth_token):
    booking_data = create_booking_payload(
        firstname="Partial",
        lastname="Before",
        totalprice=85,
        depositpaid=False,
        checkin="2025-09-10",
        checkout="2025-09-15",
        additionalneeds="Breakfast",
    )

    create_response = booking_api.create_booking(booking_data)
    validate_status_code(create_response, 200)
    booking_id = create_response.json()["bookingid"]

    partial_payload = {"lastname": "PartialUpdated", "totalprice": 95}
    partial_response = booking_api.partial_update_booking(booking_id, partial_payload, auth_token)
    validate_status_code(partial_response, 200)

    updated_booking = partial_response.json()
    assert updated_booking["lastname"] == partial_payload["lastname"]
    assert updated_booking["totalprice"] == partial_payload["totalprice"]
    assert updated_booking["firstname"] == booking_data["firstname"]
