from utils.helpers import validate_status_code
from utils.payloads import create_booking_payload


def test_delete_booking(booking_api, auth_token):
    booking_data = create_booking_payload(
        firstname="Delete",
        lastname="Me",
        totalprice=70,
        depositpaid=False,
        checkin="2025-11-01",
        checkout="2025-11-05",
        additionalneeds="None",
    )

    create_response = booking_api.create_booking(booking_data)
    validate_status_code(create_response, 200)
    booking_id = create_response.json()["bookingid"]

    delete_response = booking_api.delete_booking(booking_id, auth_token)
    validate_status_code(delete_response, 201)

    get_response = booking_api.get_booking(booking_id)
    assert get_response.status_code == 404
