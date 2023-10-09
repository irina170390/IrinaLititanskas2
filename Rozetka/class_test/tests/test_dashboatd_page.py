import time


def test_go_to_backpacks_and_bags(dashboard):
    dashboard.go_to_bags_and_backpacks()
    time.sleep(5)


def test_search_for_torba(dashboard):
    dashboard.search_for_torba('Torba na laptopa Targus Notebook Case 16&quot; czarna (CN31)')
    time.sleep(10)


def test_search_for_torba(dashboard):
    dashboard.search_for_torba('Torba na laptopa Targus Notebook Case 16&quot; czarna (CN31)')
    dashboard.wait_until_element_appears(dashboard.locators.h1_header)
    h1 = dashboard.wait_until_element_appears(dashboard.locators.h1_header)
    assert h1.text == 'Результати пошуку «Torba na laptopa Targus Notebook Case 16&quot; czarna (CN31)»'