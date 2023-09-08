from pages.base_page import BasePage
from pages.category_page import CategoryPage
from core.dashboard_locators import DashboardLocators

class Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.go_to_bags_and_backpacks_locator = ('xpath', '//a[@href="https://rozetka.pl/torby-plecaki-i-etui-na-laptopy-80036/c80036/"]/a[@href="https://rozetka.pl/akcesoria-elektroniczne-80256/c80256/"]')

    def go_to_bags_and_backpacks(self):
        locator = ('xpath', '//h1[@class="catalog-heading ng-star-inserted"]')
        self.click_on_element(self.locator.bags_and_backpacks)
        return CategoryPage(self._driver)

    def go_to_login_form(self):
        locator = ('xpath', '//a[@class="modal__background modal__background_show_animation"]')
        self.click_on_element(self.locator.login)


    def search_for_game(self, message):
        locator = ('xpath', '//img[@alt="LEGO Friends Dom rodziny Andrei 802 elementy (41449)"]')
        self.send_keys_into_field(self.locator.search, message)
        self.wait_until_element_appears(self.locator.first_search_result)
        self.press_enter(self.locator.search)




