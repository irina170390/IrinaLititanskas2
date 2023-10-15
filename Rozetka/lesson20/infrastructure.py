from requests import get, Response
from Rozetka.lesson20.test_planets.app_planets import config


class PlanetsService():
    def __init__(self):
        self.__planets_url = f"{config['host']}/planets"

    def get_planets(self, planets_id) -> Response:
        return get(f"{self.__planets_url}/{planets_id}")