from code_for_testing2 import LagerRestaurant
import pytest


a = "positions,expected"
@pytest.mark.xfail(reason='failed due to known bug @83483289')
def test_change_positions():
    lagerrestaurant = LagerRestaurant('Risotto', 'lager', 0)
    lagerrestaurant.change_positions('hardened')
    assert lagerrestaurant.positions == 'blacak'

@pytest.mark.skip('this test would be skipped')
def test_number_growth(lagerrestaurant):
    lagerrestaurant.grow()
    assert lagerrestaurant.number == 1


@pytest.mark.smoke
@pytest.mark.regression
def test_number_growth2(lagerrestaurant):
    lagerrestaurant.grow()
    assert lagerrestaurant.number == 1


@pytest.mark.parametrize(
    a, [('lager','lager'),('hardened','hardened')],ids=['change to lager', 'change to hardened']
)
def test_change_positions2(lagerrestaurant, positions, expected):
    lagerrestaurant.change_positions(positions)
    assert lagerrestaurant.positions == expected

def test_check_raise_for_exception(lagerrestaurant):
    with pytest.raises(Exception):
        lagerrestaurant.change_positions('ginger')
