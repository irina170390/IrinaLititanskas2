import json
import csv
import pytest


@pytest.mark.smoke
def test_read_json(json_converter):
    json_file = 'example.json'
    json_converter.read_json(json_file)
    assert len(json_converter._JSONConverter__lines) == 3


@pytest.mark.smoke
def test_write_csv(json_converter):
    csv_file = 'example.csv'
    json_converter._JSONConverter__lines = [
        {"first_name": "Elizabet", "last_name": "Fork", "age": "19", "gender": "Female", "salary": "3000"},
        {"first_name": "Reginald", "last_name": "Lidoo", "age": "42", "gender": "Male", "salary": "2500"},
        {"first_name": "Alexander", "last_name": "Great", "age": "30", "gender": "Male", "salary": "15000"}
    ]
    json_converter.write_csv(csv_file)

    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)
        assert len(data) == 3
        assert data[0]['first_name'] == 'Elizabet'
        assert data[1]['last_name'] == 'Lidoo'
        assert data[2]['salary'] == '15000'


@pytest.mark.regression
def test_clear_data(json_converter):
    json_converter._JSONConverter__lines = [
        {"first_name": "Elizabet", "last_name": "Fork", "age": "19", "gender": "Female", "salary": "3000"},
        {"first_name": "Reginald", "last_name": "Lidoo", "age": "42", "gender": "Male", "salary": "2500"},
        {"first_name": "Alexander", "last_name": "Great", "age": "30", "gender": "Male", "salary": "15000"}
    ]
    json_converter.clear_data()
    assert len(json_converter._JSONConverter__lines) == 0
