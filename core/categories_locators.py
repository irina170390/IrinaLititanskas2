from core.base_locators import BaseLocator


class CategoriesLocator(BaseLocator):
    def __init__(self):
        super().__init__()
        self.bags_new = ('xpath', "//h1[@class='catalog-heading ng-star-inserted']")
        self.results = ('xpath', '//a[@href="https://rozetka.pl/376667652/p376667652/"]')
        