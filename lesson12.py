import datetime
from abc import ABC, abstractmethod
import datetime
current_station = ''


class Train:
  def __init__(self, name):
    self.name = name
    self.cars = {}

  def __len__(self):
    return len(self.cars)

  def __setitem__(self, number, car):
    self.cars[number] = car

  def __getitem__(self, item):
    return self.cars[item]

  def __str__(self):
    return f' Welcome on board {self.name}! This train contains {self.__len__()} cars!'


class TrainCar(Train):

  def __init__(self, number):
    self.number = number
    self.passengers = {}

  def __len__(self):
    return len(self.passengers)

  def __setitem__(self, number, name):
    self.passengers[number] = name

  def __getitem__(self, item):
    return self.passengers[item]

  def __str__(self):
    return f' There are {self.__len__()} passengers in the car number {self.number}'


class Passenger(TrainCar):

  def __init__(self, name, seat, destination):
    self.name = name
    self.seat = seat
    self.destination = destination

  def __str__(self):
    return f'Name: {self.name}\nSeat: {self.seat}\nDestination: {self.destination}'




