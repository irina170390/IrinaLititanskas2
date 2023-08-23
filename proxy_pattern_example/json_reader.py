from.reader import Reader

class JsonReader:
    def __init__(self, filename:str):
        self.__filename = filename

    def read(self):
        with open(self.__filename, 'r') as json_file:
            text = json_file.read()
        return text