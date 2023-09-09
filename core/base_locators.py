
class BaseLocator:
    def __init__(self):
        self.login = ('xpath', '//a[@title="Вхід"]')
        self.catalog = ('xpath', "//a[text()='Katalog']")
        self.bags_and_backpacks = ('xpath', '//a[@href="https://rozetka.pl/torby-plecaki-i-etui-na-laptopy-80036/c80036/"]')
        self.search = ('xpath', '//input[@name="search"]')
        self.first_search_result = ('xpath', '//div[@class="goods-tile__actions ng-star-inserted"]')
