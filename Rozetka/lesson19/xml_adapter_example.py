from xml.etree import ElementTree
import json
import xml.etree.ElementTree as ET


class Movie:
    def __init__(self,
                 title,
                 format,
                 year,
                 rating,
                 description,
                 category):
        self.title = title
        self.format = format
        self.year = year
        self.rating = rating
        self.description = description
        self.category = category

    @classmethod
    def from_xml(cls, path):
        tree = ElementTree.parse(path)
        collection = tree.getroot()
        movies = []
        for genre in collection:
            for decade in genre:
                for movie in decade:
                    movies.append(cls(
                        movie.attrib['title'],
                        movie.find('format').text,
                        movie.find('year').text,
                        movie.find('rating').text,
                        movie.find('description').text,
                        genre.attrib['category']
                    ))
        return movies


    @staticmethod
    def xml_to_string(path):
        tree = ET.parse(path)
        root = tree.getroot()
        print(ET.tostring(root))


    @staticmethod
    def xml_to_string2():
        xml = ElementTree.Element("Person", Name="John")
        xml_to_string = ElementTree.tostring(xml, encoding='unicode')
        print(xml_to_string())

movies = Movie.from_xml("films.xml")
for movie in movies:
    print(movie.title)

movie2 = Movie.xml_to_string('films.xml')
print(movie2)

movies = Movie.from_xml("films.xml")
for movie in movies:
    print(movie.title)
