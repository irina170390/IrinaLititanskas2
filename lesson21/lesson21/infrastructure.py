import requests


base_url = "https://api.restful-api.dev/objects"


def get_single_object(object_id):
    url = f"{base_url}/{object_id}"
    response = requests.get(url)
    return response


def add_object(data):
    url = base_url
    headers = {"content-type": "application/json"}
    response = requests.post(url, json=data, headers=headers)
    return response, response.json()['id']


def update_an_object(object_id, data):
    url = f"{base_url}/{object_id}"
    headers = {"content-type": "application/json"}
    response = requests.put(url, json=data, headers=headers)
    return response


def patch_an_object(object_id, data):
    url = f"{base_url}/{object_id}"
    headers = {"content-type": "application/json"}
    response = requests.patch(url, json=data, headers=headers)
    return response


def delete_an_object(object_id):
    url = f"{base_url}/{object_id}"
    response = requests.delete(url)
    return response