from abc import ABC, abstractmethod


class RisottoRestaurant(ABC):
    _beer_type = ''

    @abstractmethod
    def get_risotto(self, name):
        pass