from lesson13.dishes import Dish, Risotto, Pasta, Pizza
from lesson13.drink import Drink, Juice, Tea


class OrderPart:
    def __init__(self):
        self.dishes = []
        self.drinks = []

    def add_dish(self, name: Dish):
        self.dishes.append(name.get_name())

    def add_drink(self, name: Drink):
        self.drinks.append(name.get_name())

    def get_dishes(self):
        return self.dishes

    def get_drinks(self):
        return self.drinks


make_order = OrderPart()

make_order.add_dish(Risotto())
make_order.add_dish(Pasta())
make_order.add_dish(Pizza())

make_order.add_drink(Juice())
make_order.add_drink(Tea())

total_dishes = make_order.get_dishes()
print("Your ordered dishes:", ", ".join(total_dishes))

total_drinks = make_order.get_drinks()
print("Your ordered drinks:", ", ".join(total_drinks))