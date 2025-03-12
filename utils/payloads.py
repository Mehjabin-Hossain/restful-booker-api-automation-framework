def create_booking_payload(
    firstname: str,
    lastname: str,
    totalprice: int,
    depositpaid: bool,
    checkin: str,
    checkout: str,
    additionalneeds: str = "Breakfast",
) -> dict:
    return {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": {
            "checkin": checkin,
            "checkout": checkout,
        },
        "additionalneeds": additionalneeds,
    }


def update_booking_payload(payload: dict, **overrides) -> dict:
    updated = payload.copy()
    updated.update(overrides)
    return updated


def partial_update_payload(**fields) -> dict:
    return fields
