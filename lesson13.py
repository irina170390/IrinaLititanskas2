class Chocolate_Milk:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

Chocolate1 = Chocolate_Milk("Milka", "AVK", 99)
Chocolate2 = Chocolate_Milk("Millenium", "Roshen", 55)
print(Chocolate1.name)
print(Chocolate2.brand)













from abc import ABC, abstractmethod
import datetime

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def open_restaurant(self):
        print("Restaurant is open right now!\n")

    def describe_restaurant(self):
        print(
            f"The name of the restaurant is {self.restaurant_name} and this restaurant have {self.cuisine_type} products, number of served: {self.number_served}")


    def update_resved(self, served):
     self.number_served = served

     if served >= self.number_served:
      self.number_served = served
     else:
      print("You can't enter negatice number of visitors")


    def increment_number_served(self, served):
      self.number_served += served


rest = Restaurant('Italiano', 'Italia', 10)
rest.describe_restaurant()
rest.open_restaurant()
rest.describe_restaurant()


class Factory(ABC):
    def flow(self):
        pass


class Dish(Factory):

    def __init__(self, dishes, quantity, beverages):
        self.dishes = dishes
        self.quantity = quantity
        self.beverages = beverages

    def start (self):
        print('Order is accepted')

    def menu (self):
         print('Risotto', 'Pasta', 'Pizza', 'Beverages')

    def stop (self):
        print('Order completed')

    def describe_restaurant(self):
        print(
        f"'Risotto', 'Pasta', 'Pizza' {self.dishes} and 4 {self.quantity} Beverages: {self.beverages}")



t = Dish('Risotto', 4, 'Juice')













