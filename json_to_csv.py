import csv
import json


class JSONConverter:
    def __init__(self):
        self.__lines = []

    def read_json(self, filename: str):
        with open(filename, 'r') as json_file:
            self.__lines = json.load(json_file)
            print(self.__lines)

    def write_csv(self, filename: str):
        with open(filename, 'w', newline='') as csv_file:
            fieldnames = self.__lines[0].keys()
            lines = csv.DictWriter(csv_file, fieldnames=fieldnames)
            lines.writeheader()
            lines.writerows(self.__lines)
            self.clear_data()

    def clear_data(self):
        self.__lines = []


converter = JSONConverter()
converter.read_json('example.json')
converter.write_csv('example_converted.csv')