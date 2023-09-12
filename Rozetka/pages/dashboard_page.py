from Rozetka.pages.base_page import BasePage
from Rozetka.pages.category_page import CategoryPage
from Rozetka.core.dashboard_locators import DashboardLocators

class Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = DashboardLocators()

    def go_to_bags_and_backpacks(self):
        self.click_on_element(self.locator.catalog)
        self.click_on_element(self.locator.bags_and_backpacks)
        return CategoryPage(self._driver)

    def go_to_login_form(self):
        self.click_on_element(self.locator.login)


    def search_for_game(self, message):
        self.click_on_element(self.locator.catalog)
        self.send_keys_into_field(self.locator.search, message)
        self.wait_until_element_appears(self.locator.first_search_result)
        self.press_enter(self.locator.search)




