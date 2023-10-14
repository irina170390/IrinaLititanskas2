from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_01():
    driver = Chrome()
    driver.get('https://rozetka.com.ua/notebook-bags/c80036/')
    search_field_locator = "//a[@href='https://rozetka.com.ua/rivacase_8037_black/p38858304/']"
    driver.implicitly_wait(10)
    element = driver.find_element(by='xpath', value=search_field_locator)
    element.send_keys('Сумка для ноутбука RivaCase 8037 Black 15.6" (8037 (Black))')
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    action.key_down(Keys.CONTROL).send_keys('x').key_up(Keys.CONTROL).perform()


def test_02():
    driver = Chrome()
    driver.get('https://rozetka.pl/')
    web_driver_wait = WebDriverWait(driver, 3)
    search_input_locator = '//input[@placeholder="Czego szukasz?"]'
    search_input_with_wait = web_driver_wait.until(EC.presence_of_element_located(('xpath', search_input_locator,)))
    search_input_with_wait.send_keys('Torba na laptopa Targus Notebook Case 16" czarna (CN31)')
    search_first_result_locator = '//div[@class="search-results__title"][1]'
    search_first_result_with_wait = web_driver_wait.until(EC.presence_of_element_located(('xpath', search_first_result_locator,)))
    assert search_first_result_with_wait.text == 'Torby, plecaki i etui na laptopy: Torba na laptopa Targus Notebook Case 16" czarna (CN31)'
    #search_input = driver.find_element(by='xpath', value=search_input_locator)