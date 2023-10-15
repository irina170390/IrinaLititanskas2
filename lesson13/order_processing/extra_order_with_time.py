from datetime import datetime
from lesson13.dishes import Dish, Risotto, Pasta, Pizza
from lesson13.drink import Drink, Juice, Tea
from lesson13.order_processing import Order


class OrderPart:
    def __init__(self):
        self.timestamp = datetime.now()
        self.order = Order(self.timestamp)

    def add_dish(self, name: Dish):
        self.order.add_item(name)

    def add_drink(self, name: Drink):
        self.order.add_item(name)

    def get_order(self):
        return self.order


make_order = OrderPart()

make_order.add_dish(Risotto())
make_order.add_dish(Pasta())
make_order.add_dish(Pizza())