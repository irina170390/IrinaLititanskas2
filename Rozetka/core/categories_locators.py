from Rozetka.core.base_locators import BaseLocator


class CategoriesLocator(BaseLocator):
    def __init__(self):
        super().__init__()
        self.checkbox_new = ('xpath', "//img[@alt='Laptopy']")
        self.results = ('xpath', '//alt[@@alt="Torba na laptopa Targus Notebook Case 16&quot; czarna (CN31)"]')
