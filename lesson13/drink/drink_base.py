from abc import ABC, abstractmethod


class Drink(ABC):

    @abstractmethod
    def get_name(self):
        pass