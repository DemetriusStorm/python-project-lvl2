"""Test formats."""

from gendiff import parsers, formats
from gendiff.gendiff import generate_diff

PATH = './tests/fixtures'


def test_json():
    """Test json."""
    with open(
            '{0}{1}'.format(PATH, '/expected/json_result'),
            'r',
    ) as source_data:
        expected = source_data.read()
        first_file = parsers.get_data(
            '{0}{1}'.format(PATH, '/data/before.json'),
        )
        second_file = parsers.get_data(
            '{0}{1}'.format(PATH, '/data/after.json'),
        )

        diff = generate_diff(first_file, second_file)
        assert formats.json(diff) == expected


def test_plain():
    """Test plain."""
    with open(
            '{0}{1}'.format(PATH, '/expected/plain_result'),
            'r',
    ) as source_data:
        expected = source_data.read()
        first_file = parsers.get_data(
            '{0}{1}'.format(PATH, '/data/before.json'),
        )
        second_file = parsers.get_data(
            '{0}{1}'.format(PATH, '/data/after.json'),
        )

        diff = generate_diff(first_file, second_file)
        assert formats.plain(diff) == expected


def test_simple_plain():
    """Test simple text."""
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

        first_file = parsers.get_data(
            '{0}{1}'.format(PATH, '/data/first_file.json'),
        )
        second_file = parsers.get_data(
            '{0}{1}'.format(PATH, '/data/second_file.json'),
        )

        diff = generate_diff(first_file, second_file)
        assert formats.simple(diff) == expected


def test_tree():
    """Test tree."""
    with open(
            '{0}{1}'.format(PATH, '/expected/complex_result.txt'),
            'r',
    ) as source_data:
        expected = source_data.read()
        first_file = parsers.get_data(
            '{0}{1}'.format(PATH, '/data/before.json'),
        )
        second_file = parsers.get_data(
            '{0}{1}'.format(PATH, '/data/after.json'),
        )

        diff = generate_diff(first_file, second_file)
        assert formats.simple(diff) == expected
