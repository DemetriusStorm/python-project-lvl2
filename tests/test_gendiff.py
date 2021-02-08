"""Test generate_diff."""

from gendiff import gendiff, parsers, formats

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

        diff = gendiff.generate_diff(first_file, second_file)
        assert formats.render_simple(diff) == expected
