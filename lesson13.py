class b:
    x = 5
y = b()
isinstance(y,b)

isinstance(b, object)
# True
type(b) == object
# False
issubclass(type(b), object)
# True


class a:
    list1 = []  # При объявлении свойства класса self не применяется
    def add_units(self, clas, num):
        for i in range(num):
            self.list1.append(clas())  # Создаём экземпляр класса clas, вызывая ()

A = a()  # Необходимо создать объект класса, чтобы вызвать его нестатический метод

A.add_units(b, 3)

print(a.list1[1].x)


class Employee:
    """Базовый класс для всех сотрудников"""
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_count(self):
        print('Всего сотрудников: %d' % Employee.empCount)

    def display_employee(self):
        print('Имя: {}. Зарплата: {}'.format(self.name, self.salary))

# Это создаст первый объект класса Employee
emp = Employee("Андрей", 2000)
emp.display_employee()
print("Всего сотрудников: %d" % Employee.emp_count)










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













