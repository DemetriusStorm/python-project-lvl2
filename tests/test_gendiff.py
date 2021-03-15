"""Test generate_diff."""

import json

import pytest

from gendiff.gendiff import generate_diff

json_file = 'tests/fixtures/json_result'
plain_file = 'tests/fixtures/plain_result'
stylish_file = 'tests/fixtures/stylish_result'


def _read_data(file_name):
    with open(file_name, 'r') as source_file:
        result_data = source_file.read()

    return result_data


@pytest.mark.parametrize('file_format', ['json', 'yml'])
def test_gen_diff(file_format):
    file1 = 'tests/fixtures/first_file.{0}'.format(file_format)
    file2 = 'tests/fixtures/second_file.{0}'.format(file_format)
    source_data = generate_diff(file1, file2, 'json')

    assert generate_diff(file1, file2) == _read_data(stylish_file)
    assert generate_diff(file1, file2, 'stylish') == _read_data(
        stylish_file,
    )
    assert generate_diff(file1, file2, 'plain') == _read_data(plain_file)
    assert isinstance(json.loads(source_data), dict)
