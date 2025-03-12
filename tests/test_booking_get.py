from utils.helpers import validate_status_code


def test_get_all_booking_ids(booking_api):
    response = booking_api.get_booking_ids()
    validate_status_code(response, 200)
    booking_list = response.json()
    assert isinstance(booking_list, list)
    assert all("bookingid" in item for item in booking_list)


def test_get_booking_by_id(booking_api):
    ids_response = booking_api.get_booking_ids()
    validate_status_code(ids_response, 200)
    booking_list = ids_response.json()
    assert booking_list, "Expected at least one booking ID"

    booking_id = booking_list[0]["bookingid"]
    booking_response = booking_api.get_booking(booking_id)
    validate_status_code(booking_response, 200)
    booking_json = booking_response.json()
    assert booking_json["firstname"], "Firstname should be present"
    assert booking_json["lastname"], "Lastname should be present"
    assert booking_json["bookingdates"], "Booking dates should be present"
