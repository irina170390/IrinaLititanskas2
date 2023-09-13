from selenium.webdriver import Chrome
from Rozetka.pages.dashboard_page import Dashboard
import pytest


@pytest.fixture
def driver():
    driver = Chrome()
    driver.get('https://rozetka.pl/')
    driver.maximize_window()

    yield driver
    driver.close()


@pytest.fixture
def dashboard(driver):
    yield Dashboard(driver)
