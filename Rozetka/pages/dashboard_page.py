from Rozetka.pages.base_page import BasePage
from Rozetka.pages.category_page import CategoryPage
from Rozetka.core.dashboard_locators import DashboardLocators
from Rozetka.pages.bags_and_backpacks import ProductPage

class Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = DashboardLocators()

    def go_to_bags_and_backpacks(self):
        locator = ('xpath','//a[@href="https://rozetka.pl/torby-plecaki-i-etui-na-laptopy-80036/c80036/"]')
        self.click_on_element(locator)
        return ProductPage(self._driver)


    def go_to_login_form(self):
        locator = ('xpath', '//a[@title="Вхiд"]')
        self.click_on_element(locator)

    def search_for_torba(self, message):
        locator = ('xpath', '//input[@_ngcontent-rz-client-c670280251]')
        self.click_on_element(self.locator.catalog)
        self.send_keys_into_field(self.locator.search, message)
        self.wait_until_element_appears(self.locator.first_search_result)
        self.press_enter(self.locator.search)




