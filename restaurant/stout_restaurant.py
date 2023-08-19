from restaurant.restaurant import RisottoRestaurant


class StoutRestaurant(RisottoRestaurant):
    _beer_type = 'stout'

    def __init__(self):
        self.name = 'Risotto'
        self.__positions = ['classic', 'rice']

    @property
    def positions(self):
        return self.__positions

    def get_beer(self, name):
        if name == 'classic':
            return 'rice'
        elif name == 'Risotto':
            return 'Risotto'