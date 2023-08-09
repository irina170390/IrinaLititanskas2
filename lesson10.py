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



    # Driver code


t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()
d = Duster()
d.mileage()

auto = Auto()
auto.mileage()
auto.mileage_from_second_parent()
