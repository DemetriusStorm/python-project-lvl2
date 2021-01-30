"""Test formats."""

from gendiff import gendiff, parsers, formats

PATH = './tests/fixtures'


def test_json():
    """Test json."""
    with open(PATH + '/expected/json_result', 'r') as f:
        expected = f.read()
        first_file = parsers.get_data(PATH + '/data/before.json')
        second_file = parsers.get_data(PATH + '/data/after.json')

        diff = gendiff.gen_diff(first_file, second_file)
        assert formats.json(diff) == expected


def test_plain():
    """Test plain."""
    with open(PATH + '/expected/plain_result', 'r') as f:
        expected = f.read()
        first_file = parsers.get_data(PATH + '/data/before.json')
        second_file = parsers.get_data(PATH + '/data/after.json')

        diff = gendiff.gen_diff(first_file, second_file)
        assert formats.plain(diff) == expected


def test_simple_plain():
    """Test simple text."""
    with open(PATH + '/expected/simple_result', 'r') as f:
        expected = f.read()
        first_file = parsers.get_data(PATH + '/data/first_file.yaml')
        second_file = parsers.get_data(PATH + '/data/second_file.yaml')

        diff = gendiff.gen_diff(first_file, second_file)
        assert formats.simple(diff) == expected

        first_file = parsers.get_data(PATH + '/data/first_file.json')
        second_file = parsers.get_data(PATH + '/data/second_file.json')

        diff = gendiff.gen_diff(first_file, second_file)
        assert formats.simple(diff) == expected


def test_tree():
    """Test tree."""
    with open(PATH + '/expected/complex_result.txt', 'r') as f:
        expected = f.read()
        first_file = parsers.get_data(PATH + '/data/before.json')
        second_file = parsers.get_data(PATH + '/data/after.json')

        diff = gendiff.gen_diff(first_file, second_file)
        assert formats.simple(diff) == expected
