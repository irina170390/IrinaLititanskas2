from pages.base_page import BasePage

class Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_bags_and_backpacks(self):
        locator = ('xpath', '//div[@class="goods-tile__actions ng-star-inserted"]/a[@href="https://rozetka.com.ua/rivacase_8037_black/p38858304/"')
        element = self.wait_until_element_appears(locator)
        element.click()

    def go_to_login_form(self):
        locator = ('xpath', '//a[@title="Вхід"]')
        element = self.wait_until_element_appears(locator)
        element.click()