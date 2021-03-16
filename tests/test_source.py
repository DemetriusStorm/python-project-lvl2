"""Test source."""

from gendiff.reader_ext_source import result_parser


def test_source():
    good_file = 'tests/fixtures/first_file.json'
    bad_file = 'tests/fixtures/first_file'

    assert isinstance(result_parser(good_file), dict)
    try:
        result_parser(bad_file)
    except FileNotFoundError as file_err:
        assert isinstance(file_err, Exception)
    except SystemExit as exit_err:
        assert isinstance(exit_err, BaseException)
