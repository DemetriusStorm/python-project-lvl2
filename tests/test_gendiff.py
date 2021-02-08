"""Test generate_diff."""

from gendiff import parsers, formats
from gendiff.gendiff import generate_diff

PATH = './tests/fixtures'


def test_generate_diff():
    """Test parse data."""
    with open(
            '{0}{1}'.format(PATH, '/expected/simple_result'),
            'r',
    ) as source_data:
        expected = source_data.read()
        first_file = parsers.get_data(
            '{0}{1}'.format(PATH, '/data/first_file.yaml'),
        )
        second_file = parsers.get_data(
            '{0}{1}'.format(PATH, '/data/second_file.yaml'),
        )

        diff = generate_diff(first_file, second_file)
        assert formats.simple(diff) == expected
