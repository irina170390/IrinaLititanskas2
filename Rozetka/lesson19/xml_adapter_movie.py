from xml.etree import ElementTree
import json


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

    def to_xml_string(self):
        movie_element = ElementTree.Element("movie", title=self.title)
        format_element = ElementTree.SubElement(movie_element, "format")
        format_element.text = self.format
        year_element = ElementTree.SubElement(movie_element, "year")
        year_element.text = self.year
        rating_element = ElementTree.SubElement(movie_element, "rating")
        rating_element.text = self.rating
        description_element = ElementTree.SubElement(movie_element, "description")
        description_element.text = self.description
        return ElementTree.tostring(movie_element, encoding="utf-8").decode("utf-8")

    @classmethod
    def from_xml_string(cls, xml_string):
        root = ElementTree.fromstring(xml_string)
        title = root.attrib['title']
        format = root.find('format').text
        year = root.find('year').text
        rating = root.find('rating').text
        description = root.find('description').text
        category = root.attrib.get('category', '')
        return cls(title, format, year, rating, description, category)

    def save_to_json(self, json_path):
        data = {
            'title': self.title,
            'format': self.format,
            'year': self.year,
            'rating': self.rating,
            'description': self.description,
            'category': self.category
        }
        with open(json_path, 'w') as json_file:
            json.dump(data, json_file)


movies = Movie.from_xml("films.xml")
xml_strings = [movie.to_xml_string() for movie in movies]

all_movies_xml = ''.join(xml_strings)
print(all_movies_xml)

all_decoded_movies = [Movie.from_xml_string(xml_string) for xml_string in xml_strings]
for decoded_movie in all_decoded_movies:
    print(decoded_movie.title)

for decoded_movie in all_decoded_movies:
    json_file_name = f"{decoded_movie.title.replace(':', '')}.json"
    decoded_movie.save_to_json(json_file_name)
