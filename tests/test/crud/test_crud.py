from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.utils.utils import Util
from src.helpers.payloads import *
from src.helpers.common_verification import *
import allure
import pytest

class TestCreateBooking:
    @pytest.fixture(scope="session")
    def create_token(self):
        response = post_request(
            url=APIConstants.url_create_token(),
            auth=None,
            headers=Util.common_header_json(),
            payload=payload_create_token(),
            in_json=False
        )

        responsecode = response.status_code
        token = response.json().get("token")
        verify_http_status_code(responsecode, 200)
        verify_response_key_should_not_be_null(token)
        return token

    @pytest.fixture(scope="session")
    def get_booking_id(self):
        response = post_request(
            url=APIConstants.url_create_booking(),
            auth=None,
            headers=Util.common_header_json(),
            payload=payload_create_booking_dynamic(),
            in_json=False
        )

        bookingid = response.json().get("bookingid")
        actual_status_code = response.status_code
        verify_http_status_code(response_data=actual_status_code, expected_data=200)
        verify_response_key_should_not_be_null(bookingid)
        return bookingid

    def test_update_booking(self,create_token,get_booking_id):
        token=create_token
        booking_id=get_booking_id
        url=APIConstants.url_patch_put_delete(booking_id=booking_id)
        response=put_patch_request(url=url,
                                   auth=None,
                                   headers=Util.common_header_put_patch_delete_basic_cookie(token=token),
                                   payload=payload_create_booking_dynamic(),
                                   in_json=False,
                                   method="PUT")

    def test_patch_booking(self,create_token,get_booking_id):
        token=create_token
        booking_id=get_booking_id
        url=APIConstants.url_patch_put_delete(booking_id=booking_id)
        response=put_patch_request(url=url,
                                   auth=None,
                                   headers=Util.common_header_put_patch_delete_basic_cookie(token=token),
                                   payload={"firstname":"Nitin"},in_json=False,
                                   method="PATCH")

    def test_delete_booking(self, create_token, get_booking_id):
        token = create_token
        booking_id = get_booking_id
        url = APIConstants.url_patch_put_delete(booking_id=booking_id)

        response = delete_request(
            url=url,
            auth=None,
            headers=Util.common_header_put_patch_delete_basic_cookie(token=token),
            in_json=False
        )


    def test_search(self,get_booking_id):
        booking_id=get_booking_id
        url=APIConstants.url_get_search(booking_id=booking_id)
        response=get_request(url=url,auth=None,in_json=False)
