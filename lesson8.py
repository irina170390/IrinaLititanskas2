import time
import math

import Calci

print(Calci.add(10, 5))
print(Calci.sub(10, 5))
print(Calci.mul(10, 5))
print(Calci.div(10, 5))

import My_Module

print(My_Module.name)
print(My_Module.digits[4:7])
print(My_Module.dict_var['a'])

import Calci as c

print(c.add(10, 5))
print(c.sub(10, 5))
print(c.mul(10, 5))
print(c.div(10, 5))

from Calci import add, mul

print(add(10, 5))
#print(sub(10, 5))
print(mul(10, 5))
#print(div(10, 5))

import Calci

all_functions = dir(Calci)
print(all_functions)









import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise


a = 5
b = "zero"

try:
    quotient = a / b
    print(quotient)
except ZeroDivisionError:
    print("You cannot divide by zero")
except TypeError:
    print("You must convert strings to floats or integers before dividing")
except NameError:
    print("A variable you're trying to use does not exist")









from datetime import datetime, timedelta


def add_subtrack_time(date, days, operation):
    if operation:
        date_calculated = date + timedelta(days=days)
    else:
        date_calculated = date - timedelta(days=days)
    return date_calculated


date_input = input("Введіть поточну дату та час у форматі 'YYYY-MM-DD HH:MM:SS': ")
current_date_value = datetime.strptime(date_input, __format="%Y-%m-%d %H:%M:%S")

days_value = int(input("Введіть кількість днів для додавання або віднімання: "))

while True:
    operation_input = input("Оберіть операцію додавання або віднімання +/- : ")
    if operation_input == "+":
        is_addition = True
        break
    elif operation_input == "-":
        is_addition = False
        break
    else:
        print("Значення невірне, спробуйте ще раз")

new_date = add_subtrack_time(current_date_value, days_value, is_addition)
print(new_date)











import datetime


def age_calculation(birth_date):
    current_date = datetime.datetime.now()
    current_age = (current_date - birth_date).days // 365
    age_timestamp = birth_date.timestamp()
    return current_age, age_timestamp


birthday = datetime.datetime(year=1998, month=5, day=20, hour=14, minute=15, second=00)
age, timestamp = age_calculation(birthday)
print("Точний вік:", age)
print("Timestamp:", timestamp)

