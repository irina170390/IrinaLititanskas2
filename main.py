import random
minute = random.randint(0,59)
if minute < 14:
    print("першій четверті години")
elif minute >= 15 and minute <= 29:
    print("другій четверті години")
elif minute >=30 and minute <= 44:
    print("третій четверті години")
elif minute >=45 and minute <= 59:
    print("четвертій четверті години")


birth_month = input("birth month: ")
a_int = int(birth_month)
if a_int <= 2 or a_int == 12:
     print("За вікном падав сніг")
elif a_int <= 5:
     print("Все довкола розцвітало")
elif a_int <= 8:
     print("Діти насолоджувались літніми канікулами")
elif a_int <= 11:
     print("Все довкола загоралось яскравими фарбами")
else:
    print("Не знайдено")


x = int(input("x: "))
y = int(input("y: "))
if x > 0 and y > 0:
    print('first')
elif x > 0 and y < 0:
    print('second')
elif x < 0 and y < 0:
    print('third')
elif x < 0 and y > 0:
    print('fourth')
elif x == 0 and y != 0:
    print('on x line')
elif x != 0 and y == 0:
    print('on y line')
else:
    print('on middle spot')


