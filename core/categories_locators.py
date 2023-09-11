from core.base_locators import BaseLocator


class CategoriesLocator(BaseLocator):
    def __init__(self):
        super().__init__()
        self.checkbox_new = ('xpath', "//a[text()='Damskie']")
        self.results = ('xpath', '//a[@href="https://rozetka.pl/376667652/p376667652/"]')
