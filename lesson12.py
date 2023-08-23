import datetime
from abc import ABC, abstractmethod
import datetime
current_station = ''

class Train:
  def __init__(self, name, destination, place, number, starttime):
    self.name = name
    self.destination = destination
    self.place = place
    self.number = number
    self.starttime = starttime
    self.stations = []
  numbers = list(range(1,12))
  print(numbers)



  def station_setup(self, stations):
    self.stations = stations

  def get_num(self):
      return self.number

  def get_destination(self):
    return self.destination

  def get_time(self):
    return self.starttime


  def __repr__(self) -> str:
    return f"{self.__class__.__name__}({self.number}, {self.destination})"

  def __str__(self) -> str:
    return self.__repr__()

class TrainCart :
  def __init__(self, name, destination, place, stages = []):
    self.name = name
    self.stages = stages

  def remove_passanger(self):
    for passanger in self.stages:
     if passanger.destination == current_station:
       self.stages.pop(passanger)


  def __len__(self):
    return len(self.stages)

  def __str__(self):
    return f"{self.name}({self.destination}{self.place})"

class Passenger:
  def __int__(self, name, destination, start_station):
    self.name = name
    self.destination = destination
    self.start_start = start_station

TrainCar1 = ("John Dow", 1)
TrainCar2 = ("Alicja Sklorz", 2)
TrainCar3 = ("Urszula John", 3)
TrainCar4 = ("Irena Cieślik", 4)
TrainCar5 = ("Eugenia Szkotak", 5)
TrainCar6 = ("Jan Poliwoda", 6)
TrainCar7 = ("Alfred Lubos", 7)
TrainCar8 = ("Ryszard Pagacz", 8)
TrainCar9 = ("Józef Dziurzycki", 9)
TrainCar10 = ("Bogdan Szczepanik", 10)
TrainCar11 = ["John Dow", "Alicja Sklorz", "Urszula John", "Irena Cieślik", "Eugenia Szkotak", "Jan Poliwoda", "Alfred Lubos", "Ryszard Pagacz", "Józef Dziurzycki", "Bogdan Szczepanik"]
Train_car_12 = TrainCart(12, '', '', [Passenger("John Dow", "Лондон-Гогвортс", 1), Passenger("Alicja Sklorz", "Лондон-Гогвортс", 2), Passenger("Urszula John", "Лондон-Гогвортс", 3)])
len(TrainCar11)
print(TrainCar11)
print(TrainCar1)
print(TrainCar2)
print(TrainCar3)
print(TrainCar4)
print(TrainCar5)
print(TrainCar6)
print(TrainCar7)
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




