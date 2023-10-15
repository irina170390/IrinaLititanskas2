import pytest
from Rozetka.lesson20.test_data_planets import test_data, expected_data

ids = 'test_id, expect_id'


def test_tatooine(planets_service):
    response = planets_service.get_planets("1")
    assert response.json()['name'] == 'Tatooine'


def test_alderaan(planets_service):
    response = planets_service.get_planets("2")
    assert response.json()['name'] == 'Alderaan'


def test_yavin_iv(planets_service):
    response = planets_service.get_planets("3")
    assert response.json()['name'] == 'Yavin IV'


def create_keys():
    list_of_cort = []
    for i in range(len(test_data)):
        list_of_cort.append((list(test_data.values())[i], list(expected_data.values())[i]))
    return list_of_cort


@pytest.mark.parametrize(ids, create_keys())
def test_planets(planets_service, test_id, expect_id):
    response = planets_service.get_planets(test_id)
    assert response.json() == expect_id