import csv

def add_row():
    kate = ['Kate', 33, 'google', 'Paris'],
    with open('listtocsv.csv', 'w') as file:
       writer = csv.writer(file)
       writer.writerow(kate)


def remove_row():
    with open("listtocsv.csv", "r") as file:
       for line in file:
         print(line)
    with open("listtocsv.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
          print(row[0], " - ", row[1])
    with open("listtocsv.csv", "r") as file:
       lines = file.readlines()
    del lines[1]
    with open("listtocsv.csv", "w") as file:
        file.writelines(lines)
        






def usunPsa(self, ImiePsa):

    with open('schronisko.csv', 'rb') as input, open('schronisko.csv', 'wb') as output:
        writer = csv.writer(output)
        for row in csv.reader(input):
                if row[0] == ImiePsa:
                    writer.writerow(row)
    with open(self.plik, 'r') as f:
            print(f.read())



