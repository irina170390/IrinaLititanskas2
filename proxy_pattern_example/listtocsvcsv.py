import csv

def add_row():
    kate = ['Kate', 33, 'google', 'Paris'],
    with open('listtocsv.csv', 'w') as file:
       writer = csv.writer(file)
       writer.writerow(kate)


def remove_row():
    with open(r"D:\listtocsv.csv", "r") as file:
       for line in file:
         print(line)
    with open(r"D:\listtocsv.csv", "r") as file:
       lines = file.readlines()
    del lines[1]
    with open(r"D:\listtocsv.csv", "w") as file:
        file.writelines(lines)




