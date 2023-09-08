
class BaseLocator:
    def __init__(self):
        self.login = ('xpath', '//a[@href="https://rozetka.pl/"]')
        self.catalog = ('xpath', "//button[@class='button button--medium button--with-icon menu__toggle ng-star-inserted'']]")
        self.bags_and_backpacks = ('xpath', '//a[@href="https://rozetka.pl/torby-plecaki-i-etui-na-laptopy-80036/c80036/"]/a[@href="https://rozetka.pl/akcesoria-elektroniczne-80256/c80256/"]')
        self.search = ('xpath', '//input[@name="search"]')
        self.first_search_result = ('xpath', '//div[@class="goods-tile__actions ng-star-inserted"]')
