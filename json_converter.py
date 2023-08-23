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














