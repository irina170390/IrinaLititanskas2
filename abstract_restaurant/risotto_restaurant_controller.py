from restaurant.lager_restaurant import LagerRestaurant
from restaurant.stout_restaurant import StoutRestaurant
class AbstractRisottoRestaurant:
    @staticmethod
    def get_factory(risotto_type):
        if risotto_type == 'lager':
            return LagerRestaurant()
        elif risotto_type == 'stout':
            return StoutRestaurant()

lager_factory_1 = AbstractRisottoRestaurant.get_factory('lager')
bottle_of_hardened_risotto = lager_factory_1.get_risotto('hardened')
print(bottle_of_hardened_risotto)