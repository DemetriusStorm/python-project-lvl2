"""Test generate_diff."""

import json

import pytest

from gendiff.gendiff import generate_diff

json_result = 'tests/fixtures/json_result'
plain_result = 'tests/fixtures/plain_result'
stylish_result = 'tests/fixtures/stylish_result'


def _read_data(file_name):
    with open(file_name, 'r') as source_file:
        result_data = source_file.read()

    return result_data


@pytest.mark.parametrize('file_format', ['json', 'yml'])
def test_gen_diff(file_format):
    file1 = 'tests/fixtures/first_file.{0}'.format(file_format)
    file2 = 'tests/fixtures/second_file.{0}'.format(file_format)
    json_diff = generate_diff(file1, file2, 'json')
    stylish_diff = generate_diff(file1, file2, 'stylish')
    plain_diff = generate_diff(file1, file2, 'plain')

    assert stylish_diff == _read_data(stylish_result)
    assert plain_diff == _read_data(plain_result)
    assert json.loads(json_diff) == json.loads(_read_data(json_result))
    assert isinstance(json.loads(json_diff), dict)
