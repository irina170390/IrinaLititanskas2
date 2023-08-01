value = []

while True:
    #print(sorted(value, key=len, reverse=True))
    value_temporary = input()
    if value_temporary == 'add':
        value_to_add = input('введіть нотатку')
        value.append(value_to_add)
    elif value_temporary == 'earliest':
          print(value)
    elif value_temporary == 'latest':
          print(list(reversed(value)))
    elif value_temporary == 'longest':
          print(sorted(value, key=len, reverse=True))
    elif value_temporary == 'shortest':
          print(sorted(value, key=len))
    elif value_temporary == 'Exit':
          break


values = ['this is note', 'this is notissimo', 'note', 'this is a huge long, insanely long note', 'well, anyways']
for element in values:
         print(len(element))


values = ['this is note', 'this is notissimo', 'note', 'this is a huge long, insanely long note', 'well, anyways']
values_numbers = []
for element in values:
    values_numbers.append(len(element))
    print(values_numbers)


second_element = {'this is note', 'this is notissimo'}
print(2 in element)


l1 = [10, 20, 30]
l2 = [20, 30, 10]
a = set(l1)
b = set(l2)
if a == b:
    print("Lists l1 and l2 are equal")
else:
    print("Lists l1 and l2 are not equal")


    print(len(second_element))

sorted_values = sorted(value, key = len)
sorted_values = sorted(value, key = len, reverse = True)



