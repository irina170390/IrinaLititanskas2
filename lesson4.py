list_with_doubles = [3, 6, 5, 8, 7]
list_with_doubles2 = [5, 7, 9, 2, 3]
new_set = set(list_with_doubles + list_with_doubles2)
list_with_doubles = list(new_set)
print(list_with_doubles + list_with_doubles2)

second_unique_values = {3,5,7}
third_unique_values = {2,5,8}
print(third_unique_values.union(second_unique_values))
print(third_unique_values.intersection(second_unique_values))

second_unique_values.update(third_unique_values)
print(second_unique_values)

def tpl_sort(tpl):
    for element in tpl:
        if not isinstance(element, int):
            return tpl
    return tuple(sorted(tpl))

# Тесты
print(tpl_sort((3, 6, 5, 8, 7)))
print(tpl_sort((5, 7, 9, 2, 3)))


OneList = [3, 6, 5, 8, 7]
TwoList = [5, 7, 9, 2, 3]
resultList = []
text = ""

OneList.sort()
TwoList.sort()

print("One List: " + str(OneList))
print("Two List: " + str(TwoList))

for i in OneList:
    if (i not in TwoList):
        resultList.append(i)
        resultList.sort()

for i in resultList:
    i = resultList.index(i)
    text += str(resultList[i]) + ", "

print("Result: " + str(text))








def multiple_named_parameters(**user_info):
    for key, value in user_info.items():
        print(f'{key} : {value}')

multiple_named_parameters(firs_name = 'Irina', second_name = '8')
multiple_named_parameters(firs_name = 'Marina', second_name = '6')
multiple_named_parameters(firs_name = 'Ivan', second_name = '3')

marks = {
    'Irina' : [8],
    'Marina' : [6],
    'Ivan' : [3]
}

def mean(lst):
    return sum(lst) / len(lst)
sortedIds = sorted(marks.keys(), key=lambda studentId: mean(marks[studentId]))
print('Средний бал :', sortedIds[1])


sum_of_all_marks = 0

for dict_value in marks.values():

 sum_of_all_marks += 5
 average_mark = sum_of_all_marks / len(marks)
 for mark in marks:

    if marks[mark] > average_mark:

     print(mark)







import random
names = ['alex', 'jonh', 'evelina']
name_index = random.randint(0,2)
print(names)
surname = ['Budu', 'Martun', 'Romaszko']
surname_index = random.randint(0,2)
print(surname)
location =['Florence', 'London', 'Odessa']
location_index = random.randint(0,2)
print(location)

random_people = {'name': names[name_index], 'surname' : surname[surname_index], 'location':location[location_index]}






















