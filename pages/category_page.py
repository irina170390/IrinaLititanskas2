from pages.base_page import BasePage
from pages.product_page import ProductPage
from core.categories_locators import CategoriesLocator

class CategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CategoriesLocator()

    def go_to_first_result(self):
        self.click_on_element(self.locators.results)
        return ProductPage(self._driver)

    def filter_new(self):
        self.click_on_element(self.locators.checkbox_new)