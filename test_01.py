from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time



def test_01():
    driver = Chrome()
    driver.get('https://hard.rozetka.pl/procesory-80083/c80083/')
    search_field_locator = "//img[@alt='Procesor AMD Threadripper Pro 5975WX 3.6GHz/128MB (100-100000445WOF) sWRX8 BOX']"
    time.sleep(5)
    element = driver.find_element(by='xpath', value=search_field_locator)
    element.click()
    time.sleep(5)
    header_locator = "//h1"
    second_page = driver.find_element(by='xpath', value=header_locator)
    assert second_page.text == 'Procesor AMD Threadripper Pro 5975WX 3.6GHz/128MB (100-100000445WOF) sWRX8 BOX'



def test_02():
    driver = Chrome()
    driver.get('https://rozetka.pl/search/?text=Torby,+plecaki+i+etui+na+laptopy')
    search_field_locator = "//a[@href='https://rozetka.pl/376667652/p376667652/']"
    driver.implicitly_wait(10)
    element = driver.find_element(by='xpath', value=search_field_locator)
    element.send_keys('Torba na laptopa Targus Notebook Case 16" czarna (CN31)')
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    action.key_down(Keys.CONTROL).send_keys('x').key_up(Keys.CONTROL).perform()


def test_03():
    driver = Chrome()
    driver.get('https://rozetka.pl/klocki-konstrukcyjne-dla-dzieci-97420/c97420/producer=lego/')
    search_field_locator = "//img[@alt='LEGO Friends Dom rodziny Andrei 802 elementy (41449)']"
    time.sleep(5)
    element = driver.find_element(by='xpath', value=search_field_locator)
    element.click()
    time.sleep(5)
    header_locator = "//h1"
    second_page = driver.find_element(by='xpath', value=header_locator)
    assert second_page.text == 'LEGO Friends Dom rodziny Andrei 802 elementy (41449)'



def test_04():
    driver = Chrome()
    driver.get('https://hard.rozetka.pl/monitory-80089/c80089/')
    search_field_locator = "//a[@href='https://hard.rozetka.pl/391043277/p391043277/']"
    time.sleep(5)
    element = driver.find_element(by='xpath', value=search_field_locator)
    element.click()
    time.sleep(5)
    header_locator = "//h1"
    second_page = driver.find_element(by='xpath', value=header_locator)
    assert second_page.text == 'Monitor Samsung 27" ViewFinity S7 S27A700 (LS27A700NWPXEN)'


def test_05():
    driver = Chrome()
    driver.get('https://rozetka.pl/telefony-komorkowe-80003/c80003/producer=samsung/')
    search_field_locator = "//img[@alt='Telefon komórkowy Samsung Galaxy A34 5G 6/128GB grafitowy (SM-A346BZKAEUE)']"
    time.sleep(5)
    element = driver.find_element(by='xpath', value=search_field_locator)
    element.click()
    time.sleep(5)
    header_locator = "//h1"
    second_page = driver.find_element(by='xpath', value=header_locator)
    assert second_page.text == 'Telefon komórkowy Samsung Galaxy A34 5G 6/128GB grafitowy (SM-A346BZKAEUE)'
    


