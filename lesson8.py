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








import datetime

dt_now = datetime.datetime.now()
print(dt_now)
from datetime import date
current_date = date.today()
print(current_date)
import datetime
current_date_time = datetime.datetime.now()
current_time = current_date_time.time()
print(current_time)
import datetime
attr = dir(datetime)
print(attr)
import datetime

timeobj= datetime.time(8,48,45)
print(timeobj)
import datetime
date_obj = datetime.datetime(2020,10,17)
print(date_obj)
from datetime import date
first_date = date(2023, 10, 5)
second_date = date(2023, 10, 25)
delta = second_date - first_date
print(delta)

time1 = datetime.date(2022,5,16)
time2 = datetime.date(2022,7,15)
time3 = time2-time1
print(time3)
time4 = datetime.datetime(year=2023,month=7,day=22,hour=12,minute=1,second=15)
time5 = datetime.datetime.now()
print(time5-time4)
time6 = time4 + time3
print(time6)
time7 = datetime.datetime.now().timestamp()
print(time7)
time8 = time4.timestamp()
print(time8)
time9 = time8 + 5485
time10 = datetime.datetime.fromtimestamp(time9)
print(time10)
from datetime import timedelta
d = timedelta(microseconds=-1)
(d.days, d.seconds, d.microseconds)


from datetime import timedelta
delta1 = timedelta(seconds=57)
delta2 = timedelta(hours=25, seconds=2)
delta2 != delta1
print()
delta2 == 5
print()


from datetime import timedelta
year = timedelta(days=365)
ten_years = 10 * year
ten_years
datetime.timedelta(days=3650)
ten_years.days // 365
10
nine_years = ten_years - year
nine_years
datetime.timedelta(days=3285)
three_years = nine_years // 3
three_years, three_years.days // 365
(datetime.timedelta(days=1095), 3)
print()








from datetime import datetime

# timestamp is number of seconds since 1970-01-01
timestamp = 1545730073

# convert the timestamp to a datetime object in the local timezone
dt_object = datetime.fromtimestamp(timestamp)

# print the datetime object and its type
print("dt_object =", dt_object)
print("type(dt_object) =", type(dt_object))


from datetime import datetime

# current date and time
now = datetime.now()

# convert from datetime to timestamp
ts = datetime.timestamp(now)

print("Timestamp =", ts)

#import datetime
from datetime import datetime
# get current date
now = datetime.now()

# convert current date into timestamp
timestamp = datetime.timestamp(now)

print("Date and Time :", now)
print("Timestamp:", timestamp)

#import datetime
from datetime import datetime
timestamp = 1572014192.8273

#convert timestamp to datetime object
dt_object = datetime.fromtimestamp(timestamp)

print("dt_object:", dt_object)
print("type(dt_object): ", type(dt_object))

# import datetime
from datetime import datetime
date_string = "17 August, 1990"

# format date
date_object = datetime.strptime(date_string, "%d %B, %Y")

print("date_object: ", date_object)


# import datetime
from datetime import datetime
dt_string = "12/11/2018 09:15:32"
# Considering date is in dd/mm/yyyy format
dt_object1 = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
print("dt_object1:", dt_object1)
# Considering date is in mm/dd/yyyy format
dt_object2 = datetime.strptime(dt_string, "%m/%d/%Y %H:%M:%S")
print("dt_object2:", dt_object2)

# Convert dt_object2 to Unix Timestamp
timestamp = datetime.timestamp(dt_object2)
print('Unix Timestamp: ', timestamp)

# Convert back into datetime
date_time = datetime.fromtimestamp(timestamp)
d = date_time.strftime("%c")
print("Output 1:", d)
d = date_time.strftime("%x")
print("Output 2:", d)
d = date_time.strftime("%X")
print("Output 3:", d)


