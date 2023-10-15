import requests
import lesson21.lesson21.infrastructure as infra


def test_get_single_object_3():
    response = infra.get_single_object(3)
    assert response.status_code == 200
    expected_data = {
      "id": "3",
      "name": "Apple iPhone 12 Pro Max",
      "data": {
         "color": "Cloudy White",
         "capacity GB": 512
        }
    }
    actual_data = response.json()
    assert actual_data == expected_data


def test_get_single_object_3():
    response = infra.get_single_object(3)
    assert response.status_code == 200
    assert "Apple iPhone 12 Pro Max, 512GB, Cloudy White" in response.text


def test_add_object():
    data = {
     "name": "Apple MacBook Pro 16",
     "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
        }
    }
    response, created_object_id = infra.add_object(data)
    get_response = infra.get_single_object(created_object_id)
    assert response.status_code == 200
    assert get_response.status_code == 200
    print(get_response.json())


def test_update_an_object():
    data_to_create = {
     "name": "Apple MacBook Pro 16",
     "data": {
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
        }
    }
    response, created_object_id = infra.add_object(data_to_create)
    assert response.status_code == 200
    data_to_update = {
     "name": "Apple MacBook Pro 16",
     "data": {
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
        }
    }
    update_response = infra.update_an_object(created_object_id, data_to_update)
    assert update_response.status_code == 200
    print(update_response.json())


def test_patch_an_object():
    data_to_create = {
     "name": "Apple MacBook Pro 16 (Updated Name)",
     "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
        }
    }
    response, created_object_id = infra.add_object(data_to_create)
    assert response.status_code == 200
    data_to_patch = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
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

