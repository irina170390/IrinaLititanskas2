from abc import ABC, abstractmethod


class Dish(ABC):

    @abstractmethod
    def get_name(self):
        pass