from requests import get
from Rozetka.lesson19.tests_sw.app import config


class PeopleService:
    def __int__(self):
        self.__people_url = f"{config['host']}/people"

    def get_people(self, people_id) -> Response:
        return get(f"{self.__people_url}/{people_id}")
