from pages.base_page import BasePage
from pages.category_page import CategoryPage
from core.dashboard_locators import DashboardLocators

class Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_bags_and_backpacks_locator = ('xpath', '//div[@class="header-layout"]')
        self.popular_categories_bags = ('xpath', '//a[@class="menu__link"][@href="https://rozetka.pl/torby-plecaki-i-etui-na-laptopy-80036/c80036/"]')

    def go_to_bags_and_backpacks(self):
        self.click_on_element(self.locators.bags_and_backpacks)
        return CategoryPage(self._driver)

    def go_to_login_form(self):
        self.click_on_element(self.locator.login)


    def search_for_game(self, message):
        self.send_keys_into_field(self.locator.search, message)
        self.wait_until_element_appears(self.locator.first_search_result)
        self.press_enter(self.locator.search)




