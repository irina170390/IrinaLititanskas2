from Rozetka.core.base_locators import BaseLocator
dashboard_locators_dict = {'go_to_bags_and_backpacks':('xpath', '//a[@href="https://rozetka.pl/torby-plecaki-i-etui-na-laptopy-80036/c80036/"]/a[@href="https://rozetka.pl/akcesoria-elektroniczne-80256/c80256/"]')}

class DashboardLocators(BaseLocator):
    def __init__(self):
        super().__init__()
        self.banner = ('xpath', '//img[@alt="Rozetka Logo"]')
        self.popular_categories_bags = ('xpath', '//button[@class="button button--medium button--with-icon menu__toggle ng-star-inserted"]/a[@href="https://rozetka.pl/torby-plecaki-i-etui-na-laptopy-80036/c80036/"]')
