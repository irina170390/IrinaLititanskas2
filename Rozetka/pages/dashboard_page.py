from Rozetka.pages.base_page import BasePage
from Rozetka.pages.category_page import CategoryPage
from Rozetka.core.dashboard_locators import DashboardLocators

class Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = DashboardLocators()


    def go_to_backpacks_and_bags(self):
        self.click_on_element(self.locators.catalog)
        self.click_on_element(self.locators.bags_and_backpacks)
        return CategoryPage(self._driver)



    def go_to_login_form(self):
        self.click_on_element(self.locators.login)

    def search_for_torba(self, message):
        locator = ('xpath', '//input[@_ngcontent-rz-client-c670280251]')
        self.click_on_element(self.locators.catalog)
        self.send_keys_into_field(self.locators.search, message)
        self.wait_until_element_appears(self.locators.first_search_result)
        self.press_enter(self.locators.search)




