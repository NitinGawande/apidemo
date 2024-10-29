def verify_http_status_code(response_data, expected_data):
    assert response_data == expected_data ,"The sataus code is wrong"

def verify_json_key_for_not_null(key):
    assert key !=0 ,"Key is non empty" + key
    assert key > 0 ,"Key is greather than zero"

def verify_response_key_should_not_be_null(key):
    assert key is not None,"Key is null"

