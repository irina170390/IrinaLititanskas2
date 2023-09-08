from pages.base_page import BasePage
from pages.dashboard_page import Dashboard

class ProductPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def return_to_dashboard_page(self):
        locator = ('xpath', '//a[@href="https://rozetka.pl/376667652/p376667652/"]')
        self.click_on_element(locator)
        return Dashboard(self._driver)

