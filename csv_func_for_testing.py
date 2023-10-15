import csv


class CSVController:

    def __init__(self, file_path):
        self.file_path = file_path

    def add_row(self, row_data):
        with open(self.file_path, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(row_data)

    def delete_row(self, row_index):
        rows = []
        with open(self.file_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                rows.append(row)

        with open(self.file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for index, row in enumerate(rows):
                if index != row_index:
                    csv_writer.writerow(row)