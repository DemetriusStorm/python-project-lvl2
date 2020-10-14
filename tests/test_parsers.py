"""Test data."""

from gendiff import parsers

PATH = './tests/fixtures/data'


def test_parse_data():
    """Test parse data."""
    test_cases = [
        (PATH + '/second_file.json', '.json'),
        (PATH + '/second_file.yaml', '.yaml'),
    ]

    for case in test_cases:
        assert type(parsers.result_parser(case[1], case[0])) == dict

    test_cases = [
        PATH + '/second_file.json',
        PATH + '/second_file.yaml',
    ]

    for case in test_cases:
        assert type(parsers.get_data(case)) == dict
