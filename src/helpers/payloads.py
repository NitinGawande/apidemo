from faker import Faker
faker=Faker()

def payload_create_booking():
    payload={
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    return payload



def payload_create_booking_dynamic():
    payload={
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=150, max=999),
        "depositpaid": faker.boolean(),
        "bookingdates": {
            "checkin":  faker.date(pattern="%Y-%m-%d"),
            "checkout": faker.date(pattern="%Y-%m-%d")
        },
        "additionalneeds": faker.random_element(elements=("Breakfast","Spa","Parking","Dinner","Games"))
    }
    return payload

def payload_create_token():
    payload={
        "username": "admin",
        "password": "password123"
    }
    return payload