import pytest
from Rozetka.lesson20.infrastructure import PlanetsService


@pytest.fixture()
def planets_service():
    yield PlanetsService()