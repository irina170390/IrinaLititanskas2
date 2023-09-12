
class BaseLocator:
    def __init__(self):
        self.login = ('xpath', '//svg[@aria-hidden="true"]')
        self.catalog = ('xpath', "//button[@id='fat-menu']")
        self.bags_and_backpacks = ('xpath', '//a[@href="https://rozetka.pl/torby-plecaki-i-etui-na-laptopy-80036/c80036/"]')
        self.search = ('xpath', '//input[@name="search"]')
        self.first_search_result = ('xpath', '//alt[@alt="Torba na laptopa Targus Notebook Case 16&quot; czarna (CN31)"]')
