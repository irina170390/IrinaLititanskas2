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
    driver.get('https://rozetka.com.ua/notebook-bags/c80036/')
    web_driver_wait = WebDriverWait(driver, 3)
    search_input_locator = '//input[@name="search"]'
    search_input_with_wait = web_driver_wait.until(EC.presence_of_element_located(('xpath', search_input_locator,)))
    search_input_with_wait.send_keys('Сумка для ноутбука RivaCase 8037 Black 15.6" (8037 (Black))')
    search_first_result_locator = '//a[@href="https://rozetka.com.ua/rivacase_8037_black/p38858304/"]'
    search_first_result_with_wait = web_driver_wait.until(EC.presence_of_element_located(('xpath', search_first_result_locator,)))
    assert search_first_result_with_wait.accessible_name == 'Сумка для ноутбука RivaCase 8037 Black 15.6" (8037 (Black)) Воспользуйтесь скидкой 5%'
    #search_input = driver.find_element(by='xpath', value=search_input_locator)



def test_03():
    driver = Chrome()
    driver.get('https://rozetka.com.ua/notebook-bags/c80036/')
    web_driver_wait = WebDriverWait(driver, 3)
    search_input_locator = '//input[@name="search"]'
    search_input_with_wait = web_driver_wait.until(EC.presence_of_element_located(('xpath', search_input_locator,)))
    search_input_with_wait.send_keys('Сумка для ноутбука Case Logic CHANLB115 15.6" Black (3203661)')
    search_first_result_locator = '//a[@href="https://rozetka.com.ua/case-logic-3203661/p393028527/"]'
    search_first_result_with_wait = web_driver_wait.until(EC.presence_of_element_located(('xpath', search_first_result_locator,)))
    assert search_first_result_with_wait.accessible_name == 'Сумка для ноутбука Case Logic CHANLB115 15.6" Black (3203661) Воспользуйтесь скидкой 5%'
    # search_input = driver.find_element(by='xpath', value=search_input_locator)



def test_04():
    driver = Chrome()
    driver.get('https://rozetka.com.ua/notebook-bags/c80036/')
    web_driver_wait = WebDriverWait(driver, 3)
    search_input_locator = '//input[@name="search"]'
    search_input_with_wait = web_driver_wait.until(EC.presence_of_element_located(('xpath', search_input_locator,)))
    search_input_with_wait.send_keys('Рюкзак для ноутбука Promate Satchel-BP 15.6" Black (satchel-bp.black)')
    search_first_result_locator = '//a[@href="https://rozetka.com.ua/promate-satchel-bp-black/p391173489/"]'
    search_first_result_with_wait = web_driver_wait.until(EC.presence_of_element_located(('xpath', search_first_result_locator,)))
    assert search_first_result_with_wait.accessible_name == 'Рюкзак для ноутбука Promate Satchel-BP 15.6" Black (satchel-bp.black) Воспользуйтесь скидкой 5%'
    # search_input = driver.find_element(by='xpath', value=search_input_locator)


def test_05():
    driver = Chrome()
    driver.get('https://rozetka.com.ua/notebook-bags/c80036/')
    web_driver_wait = WebDriverWait(driver, 3)
    search_input_locator = '//input[@name="search"]'
    search_input_with_wait = web_driver_wait.until(EC.presence_of_element_located(('xpath', search_input_locator,)))
    search_input_with_wait.send_keys('Сумка для ноутбука 2E Beginner 16" Dark Olive (2E-CBN315DO)')
    search_first_result_locator = '//a[@href="https://rozetka.com.ua/2e-2e-cbn315do/p379895181/"]'
    search_first_result_with_wait = web_driver_wait.until(EC.presence_of_element_located(('xpath', search_first_result_locator,)))
    assert search_first_result_with_wait.accessible_name == 'Сумка для ноутбука 2E Beginner 16" Dark Olive (2E-CBN315DO) Воспользуйтесь скидкой 5%'
    # search_input = driver.find_element(by='xpath', value=search_input_locator)



def test_06():
    driver = Chrome()
    driver.get('https://rozetka.com.ua/notebook-bags/c80036/')
    web_driver_wait = WebDriverWait(driver, 3)
    search_input_locator = '//input[@name="search"]'
    search_input_with_wait = web_driver_wait.until(EC.presence_of_element_located(('xpath', search_input_locator,)))
    search_input_with_wait.send_keys('Сумка для ноутбука 2E 17.3" Grey (2E-CBN317GY)')
    search_first_result_locator = '//a[@href="https://rozetka.com.ua/2e_2e_cbn317gy/p180269013/"]'
    search_first_result_with_wait = web_driver_wait.until(EC.presence_of_element_located(('xpath', search_first_result_locator,)))
    assert search_first_result_with_wait.accessible_name == 'Сумка для ноутбука 2E 17.3" Grey (2E-CBN317GY) Воспользуйтесь скидкой 5%'
    #search_input = driver.find_element(by='xpath', value=search_input_locator)