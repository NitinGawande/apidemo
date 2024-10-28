#API Constants - Class which contains all the endpoints
#Keep the URLs
#Static Method -> Which can be called by using object directly without using class

class APIConstants:
    @staticmethod
    def base_use():
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"

    @staticmethod
    def url_patch_put_delete(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)