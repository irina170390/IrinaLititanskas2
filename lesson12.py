import datetime
from abc import ABC, abstractmethod
import datetime

class Train:
  def __init__(self, name, destination, place, number, starttime, time):
    self.name = name
    self.destination = destination
    self.place = place
    self.number = number
    self.starttime = starttime
    self.time = time

  def get_num(self):
      return self.number

  def get_destination(self):
    return self.destination

  def get_time(self):
    return self.starttime

  def __init__(self, destination: str, number: str, departure: str):
      self.destination, self.number, self.departure = destination, number, departure

  def __repr__(self) -> str:
    return f"{self.__class__.__name__}({self.number}, {self.destination}, {self.departure})"

  def __str__(self) -> str:
    return self.__repr__()

class TrainCar :
  def __init__(self, name, destination, place):
    self.name = name
    self.destination = destination
    self.place = place
    self.stages = {}


  def __len__(self):
    return len(self.stages)

  def __str__(self):
    return f"{self.name}({self.destination}{self.place})"
TrainCar1 = ("John Dow",  "Name of station", 1)
TrainCar2 = ("Alicja Sklorz",  "Name of station", 2)
TrainCar3 = ("Urszula John",  "Name of station", 3)
TrainCar4 = ("Irena Cieślik",  "Name of station", 4)
TrainCar5 = ("Eugenia Szkotak",  "Name of station", 5)
TrainCar6 = ("Jan Poliwoda",  "Name of station", 6)
TrainCar7 = ("Alfred Lubos",  "Name of station", 7)
TrainCar8 = ("Ryszard Pagacz",  "Name of station", 8)
TrainCar9 = ("Józef Dziurzycki",  "Name of station", 9)
TrainCar10 = ("Bogdan Szczepanik",  "Name of station", 10)
TrainCar11 = ["John Dow", "Alicja Sklorz", "Urszula John", "Irena Cieślik", "Eugenia Szkotak", "Jan Poliwoda", "Alfred Lubos", "Ryszard Pagacz", "Józef Dziurzycki", "Bogdan Szczepanik"]
len(TrainCar11)
print(TrainCar11)
print(TrainCar1)
print(TrainCar2)
print(TrainCar3)
print(TrainCar4)
print(TrainCar5)
print(TrainCar6)
print(TrainCar)
print(TrainCar8)
print(TrainCar9)
print(TrainCar10)
count_TrainCar11 = len(TrainCar11)
print(count_TrainCar11)




class FreightTrain(Train):

  def __init__(self, destination, number, starttime, time):
    Train.__init__(self, destination, number, starttime)

  def __str__(self):
    return f'Пассажирский {self.number} до {self.destination} \
время отправления {self.starttime}'


class Railway:

  def __init__(self):  # изначально вокзал пуст
    self.list_train = []

  def add_train(self, train):
    # добавление поездов и их сортировка по времени
    self.list_train.append(train)
    self.list_train.sort(key=lambda x: x.get_time())


  def info_destination(self, destination):
   # вывод информации о поездах, отправляющихся в заданный пункт назначения
      for train in self.list_train:
          if destination == train.get_destination():
              print(train)

railway = Railway()


class RailwayStation:

  def __init__(self, trains: list):
    self.__trains = trains

  @property
  def trains(self) -> tuple:
    return tuple(self.__trains)

  def __getitem__(self, index: int):
    return self.__trains[index]

  def by_destination(self, destination: str) -> tuple:
    return tuple([train for train in self.__trains if train.destination == destination])

  def by_post_time(self, departure: str) -> tuple:
    return tuple([train for train in self.__trains if train.departure > departure])


STATION = RailwayStation([
  FreightTrain("Лондон-Гогвортс", "1", "2023.01.12", ["John Dow"])
])

print(STATION.by_destination("Лондон-Гогвортс"))
print(STATION.by_post_time("2023.01.12"))




