import csv
from csv_func_for_testing import CSVController


class TestCSV:

    def setup_class(self):
        self.csv_file = "example.csv"

    def test_add_row_to_csv(self):
        controller = CSVController(self.csv_file)
        new_row = ['John', 'Doe', '25', 'Male', '5000']
        controller.add_row(new_row)

        with open(self.csv_file, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            rows = list(csv_reader)
            assert new_row in rows

    def test_delete_row_from_csv(self):
        controller = CSVController(self.csv_file)
        row_index_to_delete = 1
        controller.delete_row(row_index_to_delete)

        with open(self.csv_file, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            rows = list(csv_reader)
            assert len(rows) == 3