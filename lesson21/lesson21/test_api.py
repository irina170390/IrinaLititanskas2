import requests
import lesson21.lesson21.infrastructure as infra


def test_get_single_object_5():
    response = infra.get_single_object(5)
    assert response.status_code == 200
    expected_data = {
        "id": "5",
        "name": "Apple MacBook Air",
        "data": {
            "year": 2022,
            "price": 44.999,
            "CPU model": "Air 13 M1",
            "Hard disk size": "1 TB"
        }
    }
    actual_data = response.json()
    assert actual_data == expected_data


def test_get_single_object_3():
    response = infra.get_single_object(3)
    assert response.status_code == 200
    assert "Apple MacBook Air, 256GB, midnight" in response.text


def test_add_object():
    data = {
        "name": "Apple MacBook Air",
        "data": {
            "color": "midnight",
            "generation": "3rd",
            "price": 44.999
        }
    }
    response, created_object_id = infra.add_object(data)
    get_response = infra.get_single_object(created_object_id)
    assert response.status_code == 200
    assert get_response.status_code == 200
    print(get_response.json())


def test_update_an_object():
    data_to_create = {
        "name": "Apple MacBook Air",
        "data": {
            "year": 2022,
            "price": 44.999,
            "CPU model": "Air 13 M1",
            "Hard disk size": "1 TB",
            "color": "midnight"
        }
    }
    response, created_object_id = infra.add_object(data_to_create)
    assert response.status_code == 200
    data_to_update = {
        "name": "New Apple MacBook Air",
        "data": {
            "year": 2022,
            "price": 44.999,
            "CPU model": "Air 13 M1",
            "Hard disk size": "1 TB",
            "color": "midnight"
        }
    }
    update_response = infra.update_an_object(created_object_id, data_to_update)
    assert update_response.status_code == 200
    print(update_response.json())


def test_patch_an_object():
    data_to_create = {
        "name": "Apple MacBook Air",
        "data": {
            "year": 2022,
            "price": 44.999,
            "CPU model": "Air 13 M1",
            "Hard disk size": "1 TB",
            "color": "midnight"
        }
    }
    response, created_object_id = infra.add_object(data_to_create)
    assert response.status_code == 200
    data_to_patch = {
        "name": "Apple MacBook Air (Updated Name)"
    }
    patch_response = infra.patch_an_object(created_object_id, data_to_patch)
    assert patch_response.status_code == 200
    get_response = infra.get_single_object(created_object_id)
    updated_data = get_response.json()
    assert updated_data['name'] == data_to_patch['name']
    print(updated_data)


def test_delete_an_object():
    data_to_delete = {
        "name": "Apple to delete"
    }
    response, created_object_id = infra.add_object(data_to_delete)
    assert response.status_code == 200
    delete_response = infra.delete_an_object(created_object_id)
    assert delete_response.status_code == 200
    assert "Object with id" in delete_response.json()["message"]
    print(delete_response.json())

