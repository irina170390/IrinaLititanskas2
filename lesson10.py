from abc import ABC, abstractmethod

class  Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start (self):
        print('Запуск автомобиля')

    def stop (self):
        print('Остановка автомобиля')

    def Accurate (self):
        print('Ускоряющийся автомобиль')

    @abstractmethod
    def go_straight(self):
        pass

    @abstractmethod
    def refuel(self):
        pass

class Car(ABC):
    def mileage(self):
        pass

class Tesla(Car):
    def mileage(self):
        print("The mileage is 30km")


class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25km ")


class Duster(Car):
    def mileage(self):
        print("The mileage is 24km ")


class Renault(Car):
    def mileage(self):
        print("The mileage is 27km ")


class Auto(Tesla,Suzuki,Duster,Renault):
    def mileage(self):
        print("The mileage is 100km ")

    def mileage_from_second_parent(self):
        Renault.mileage(self)

class Engineer(Tesla):
    def __init__(self, salary, position):
        super().__init__(salary, position)

    def do_work(self):
        print('I`m doing Tesla stuff')

class Tesla(object):
    """docstring"""

    def __init__(self, color, tires):
     """Constructor"""
     self.color = color
     self.tires = tires

    def brake(self):
     """
     Stop the car
     """
     return "Braking"

    def drive(self):
     """
     Drive the car
     """
     return "I'm driving!"


class Functools(Tesla):
    def open_window(self):
        print('window is opened')
    def door_close(self):
        print('the door is closed')


    # Driver code

t = Tesla('white', 4)
r = Renault()
r.mileage()

s = Suzuki()
s.mileage()
d = Duster()
d.mileage()

auto = Auto()
auto.mileage()
auto.mileage_from_second_parent()
