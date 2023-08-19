from restaurant import RisottoRestaurant
from restaurant.hardened_risotto import HardenedRisotto


class LagerRestaurant(RisottoRestaurant):
    _risotto_type = 'lager'

    def __init__(self):
        self.name = 'Risotto'
        self.__positions = ['lager', 'hardened']

    @property
    def positions(self):
        return self.__positions

    def get_beer(self, name):
        if name == 'lager':
            return 'here`s your lager'
        elif name == 'hardened':
            return HardenedRisotto()