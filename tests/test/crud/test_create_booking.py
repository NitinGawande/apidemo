import pytest
import allure
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_request
from src.helpers.payloads import payload_create_booking_dynamic
from src.utils.utils import Util
from src.helpers.common_verification import *

class TestCreateBooking:
    @pytest.mark.positive
    @allure.title("Verify that Create booking ID Status and booking ID should no be null")
    @allure.description("Creating the booking from the payload and verifying the booking ID Status and booking ID should no be null")
    def test_create_booking_positive(self):
        # URL,Header,Payload
        response=post_request(url=APIConstants.url_create_booking(),
                              auth=None,
                              headers=Util().common_header_json(),
                              payload=payload_create_booking_dynamic(),
                              in_json=False)

        bookingid=response.json()['bookingid']
        actual_status_code=response.status_code
        verify_http_status_code(response_data=actual_status_code,expected_data=200)
        verify_response_key_should_not_be_null(bookingid)

    @pytest.mark.negative
    @allure.title("Verify the status code ")
    @allure.description("Create booking with the empty payload and check the verification code")
    def test_create_booking_nagative(self):
        response = post_request(url=APIConstants.url_create_booking(),
                                auth=None,
                                headers=Util().common_header_json(),
                                payload={},
                                in_json=False)

        actual_status_code = response.status_code
        verify_http_status_code(response_data=actual_status_code, expected_data=500)



