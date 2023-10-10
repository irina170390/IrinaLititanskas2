import time


def test_go_to_backpacks_and_bags(dashboard):
    dashboard.go_to_bags_and_backpacks()
    time.sleep(5)


def test_search_for_torba(dashboard):
    dashboard.search_for_game('Torba na laptopa Targus Notebook Case 16" czarna (CN31)')
    time.sleep(10)


def test2_search_for_torba(dashboard):
    dashboard.search_for_game('torba')
    time.sleep(5)


