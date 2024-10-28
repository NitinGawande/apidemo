import json
import requests



def get_request(url,auth):
    get_response=requests.get(url=url,auth=auth)
    return get_response.json()

def post_request(url,auth,headers,payload,in_json):
    post_response=requests.post(url=url,auth=auth,headers=headers,data=json.dumps(payload))
    if in_json is True:
        return post_response.json()
    return post_response

def put_patch_request( url, auth, headers, payload, in_json):
    put_patch_response = requests.post(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return put_patch_response.json()
    return put_patch_response

def delete_request( url, auth, headers,in_json):
    delete_response = requests.post(url=url, auth=auth, headers=headers)
    if in_json is True:
         return delete_response.json()
    return delete_response
