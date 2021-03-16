"""Test formats."""

import json

import pytest
import subprocess

json_file = 'tests/fixtures/json_result'
plain_file = 'tests/fixtures/plain_result'
stylish_file = 'tests/fixtures/stylish_result'


def _read_data(file_name):
    with open(file_name, 'r') as source_file:
        result_data = source_file.read()

    return '{0}\n'.format(result_data)


def _exec_app(file_path1, file_path2, file_format=None):
    args = ['poetry', 'run', 'gendiff']

    if file_format is not None:
        args.extend(['-f', file_format])
    args.extend([file_path1, file_path2])

    return subprocess.check_output(args, universal_newlines=True)


@pytest.mark.parametrize('file_format', ['json', 'yml'])
def test_console(file_format):
    file1 = 'tests/fixtures/first_file.{0}'.format(file_format)
    file2 = 'tests/fixtures/second_file.{0}'.format(file_format)
    source_data = _exec_app(file1, file2, 'json')

    assert _exec_app(file1, file2) == _read_data(stylish_file)
    assert _exec_app(file1, file2, 'stylish') == _read_data(stylish_file)
    assert _exec_app(file1, file2, 'plain') == _read_data(plain_file)
    assert isinstance(json.loads(source_data), dict)


def test_source():
    file1 = 'tests/fixtures/first_file.json'
    file_err = 'tests/fixtures/first_file'
    try:
        _exec_app(file1, file_err, 'json')
    except subprocess.CalledProcessError as err:
        assert isinstance(err, Exception)
