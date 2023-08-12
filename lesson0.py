from abc import ABC, abstractmethod
class Car(ABC):
    def __init__(self, wheels, color, fuel_type):
        self.wheels = wheels
        self.color = color
        self.fuel_type = fuel_type

    @abstractmethod
    def go_straight(self):
        pass

    @abstractmethod
    def refuel(self):
        pass

    def open_window(self):
        print('window is opened')

class Electro(Car):
    def __init__(self, wheels, color, fuel_type):
        super().__init__(wheels, color, fuel_type)


    def go_straight(self):
        print('car going straight')

    def refuel(self):
        print('car charged')

class Gasoline(Car):
    def __init__(self, wheels, color, fuel_type):
        super().__init__(wheels, color, fuel_type)

    def go_straight(self):
        print('car going straight')

    def refuel(self):
        print('car fueled')

gasoline_car = Gasoline(5, 'white', 'gasoline')
electro_car = Electro(5, 'black', 'electricity')
gasoline_car.go_straight()
gasoline_car.refuel()
gasoline_car.open_window()
electro_car.go_straight()
electro_car.refuel()
electro_car.open_window()