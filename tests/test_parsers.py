"""Test data."""

from gendiff import reader_ext_source as reader
from gendiff import parsers

PATH = './tests/fixtures/data'


def test_parse_data():
    """Test parse data."""
    test_cases = [
        ['{0}{1}'.format(PATH, '/second_file.json'), '.json'],
        ['{0}{1}'.format(PATH, '/second_file.yaml'), '.yaml'],
    ]
    assert isinstance(
        reader.result_parser(test_cases[0][1], test_cases[0][0]),
        dict,
    )
    assert isinstance(
        reader.result_parser(test_cases[1][1], test_cases[1][0]),
        dict,
    )

    test_cases = [
        '{0}{1}'.format(PATH, '/second_file.json'),
        '{0}{1}'.format(PATH, '/second_file.yaml'),
    ]
    assert isinstance(parsers.get_data(test_cases[0]), dict)
    assert isinstance(parsers.get_data(test_cases[1]), dict)
