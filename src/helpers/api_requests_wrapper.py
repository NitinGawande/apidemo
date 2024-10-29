import json
import requests

def get_request(url, auth, in_json):
    get_response = requests.get(url=url, auth=auth)
    return get_response.json() if in_json else get_response

def post_request(url, auth, headers, payload, in_json):
    post_response = requests.post(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    return post_response.json() if in_json else post_response

def put_patch_request(url, auth, headers, payload, in_json, method="PUT"):
    """
    Handles both PUT and PATCH requests depending on the method argument.
    """
    if method == "PUT":
        put_patch_response = requests.put(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    elif method == "PATCH":
        put_patch_response = requests.patch(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    else:
        raise ValueError("Invalid method for put_patch_request. Use 'PUT' or 'PATCH'.")

    return put_patch_response.json() if in_json else put_patch_response

def delete_request(url, auth, headers, in_json):
    delete_response = requests.delete(url=url, auth=auth, headers=headers)
    return delete_response.json() if in_json else delete_response
