from .listtocsvcsv import add_row, remove_row

def test_add():
    add_row()
    with open('listtocsv.csv', 'r') as file:
        lines = file.readlines()
        assert lines == ['"[\'Kate\', 33, \'google\', \'Paris\']"\n']

def test_remove():
    add_row()
    with open('listtocsv.csv', 'r') as file:
        lines = file.readlines()
        assert lines == ['"[\'Kate\', 33, \'google\', \'Paris\']"\n']

