
def intersection_list(list1, list2):
    list3 = [list(filter(lambda x: x in list1, sublist)) for sublist in list2]
    return list3

list1 = [10, 9, 17, 40, 23, 18, 56, 49, 58, 60]
list2 = [[25, 17, 23, 40, 32], [1, 10, 13, 27, 28], [60, 55, 61, 78, 15, 76]]
print(intersection_list(list1, list2))





result = lambda x : x.isnumeric() if type(x) == str else x
print(result('5'))
print(result('a'))
print(result(5))






from functools import reduce
list_a = [20, 50, 120, 30, 80]
max_el = reduce(lambda x, y : x if (x>y) else y, list_a)
print(max_el)
min_el = reduce(lambda x, y : x if (x<y) else y, list_a)
print(min_el)

list_a = [[20, 50], [120, 30, 80], [60, 90, 200]]
max_el = reduce(lambda x, y : x if len(x)>len(y) else y, list_a)
print(max_el)
min_el = reduce(lambda x, y : x if len(x)<len(y) else y, list_a)
print(min_el)


