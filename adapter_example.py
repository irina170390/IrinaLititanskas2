import json
import csv

class JsonConverter:
    def __init__(self):
        self.__lines = []

    def read_file(self, filename:str):
        with open(filename, 'r') as json_file:
         lines = json.DictReader(json_file)
        for line in lines:
         self.__lines.append((line))
        print(self.__lines)

    def write_to_file(self, filename: str):
        with open(filename, 'w') as writer:
         csv.dump(self.__lines, writer, indent=4)
         self.cleanup()

    def cleanup(self):
         self.__lines = []

converter = JsonConverter()
converter.read_file('example.json')
converter.write_file('example.csv')
converter.read_file('example.json')
converter.write_file('example2.csv')
converter.read_file('users.json')
converter.write_to_file('users.csv')





