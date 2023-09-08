import time
from pages.base_page import BasePage

class categoryPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)


def test_go_to_first_result(dashboard):
    category_page = dashboard.go_to_bags_and_backpacks()
    product_page = category_page.go_to_first_result()
    time.sleep(5)


def test_filtered_new(dashboard):
    category_page = dashboard.go_to_bags_and_backpacks()
    category_page.filter_new()
    product_page = category_page.go_to_first_result()
    time.sleep(5)


def test_filtered_new_start_from_categories(categories):
    categories.filter_new()
    product_page = categories.go_to_first_result()
    time.sleep(5)


