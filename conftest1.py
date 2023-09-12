import pytest
from code_for_testing2 import LagerRestaurant

@pytest.fixture
def lagerrestaurant():
    print('setup for test')
    yield LagerRestaurant('Risotto', 'lager', 0)
    print('teardown for test')

