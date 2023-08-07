
class Dog:
    # Class Variable
    animal = 'dog'

    # The init method or constructor
    def __init__(self, breed, color):

        self.color = color
# Objects of Dog class
Simbo = Dog("Pug", "brown")

print('Simbo details:')
print('Simbo is a', Simbo.animal)
print('Color: ', Simbo.color)

class Dog:
    'A simple dog model.'

    def __init__(self, name, age):
        'Construct name and age attributes for an instance of Dog'
        self.name = name.title()
        self.age = age

    def sit(self):
        'Simulate a dog sitting in response to a command.'
        print(self.name + " is now sitting.")

    def roll_over(self):
        'Simulate rolling over in response to a command.'
        print(self.name + " rolled over!")

my_dog = Dog(name='simbo', age=6)

print("My dog's name is " + my_dog.name + ".")
print("My dog is " + str(my_dog.age) + " years old.")

class Employee(Dog):
    def __init__(self, name, age, salary, position):
        super().__init__(name, age)
        self.salary = salary
        self.position = position


goose = Employee('Simbo', 5, 'male', '2 glasses of wheat')
print()


class name_of_class:
   @staticmethod
   def name_of_static_method(parameters_list):
      pass
print ('static method defined')

class Animal:
   @staticmethod
   def test(a):
      print('static method', a)

   # calling a static method


Animal.test(12)
# calling using object
anm = Animal()
anm.test(12)


class Animal:
   def test(a):
      print('static method', a)
# converting to the static method
Animal.test = staticmethod(Animal.test)
# calling the static method
Animal.test(5)









class School:
    staff = 100
    students = 500
    classes = 400


    @classmethod
    def print_strength(cls):
        print(cls, cls.staff)

class Nova(School):
    pass

Nova1 = Nova()
print(Nova1.staff)
print(Nova1.students)
print(Nova1.classes)
Nova1.print_strength()


class Director (School):
    def __init__(self,salary,position):
        super().__init__(salary, position)

    def do_work(self):
        print('i`m the principal of the school')


class Teacher (School):
    def __init__(self,salary,position):
        super().__init__(salary,position)

    def do_work(self):
        print('I teach children')


class Cleaning (School):
    def __init__(self, salary, position):
        super().__init__(salary, position)

    def do_work(self):
        print('I keep the school clean')












def select(input_func):
    def output_func():
        print("*****************")
        input_func()
        print("*****************")
    return output_func

@select
def output_func():
    print("Irina")


output_func()


def add(x, y):
    return x + y

def calculate(func, x, y):
    return func(x, y)

result = calculate(add, 4, 6)
print(result)  # prints 10

def add(x, y):
    return x * y

def calculate(func, x, y):
    return func(x, y)

result = calculate(add, 4, 6)
print(result)  # prints 10









import random
randomlist = [random.randint(1, 10) for value in range(0, 100)]
print('список:', randomlist)

list_numbers = randomlist
print(list_numbers.count(1))
print(list_numbers.count(2))
print(list_numbers.count(3))
print(list_numbers.count(4))
print(list_numbers.count(5))
print(list_numbers.count(6))
print(list_numbers.count(7))
print(list_numbers.count(8))
print(list_numbers.count(9))
print(list_numbers.count(10))






















