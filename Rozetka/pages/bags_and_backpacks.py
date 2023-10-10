from Rozetka.pages.base_page import BasePage
from Rozetka.pages.dashboard_page import Dashboard


class ProductPage(BasePage):

    def __int__(self, driver):
        super().__int__(driver)



    def retutn_to_dashboard_page(self):
        locator  =('xpath', '//a[@class="header__logo"]')
        self.click_on_element(locator)
        return Dashboard(self._driver)


