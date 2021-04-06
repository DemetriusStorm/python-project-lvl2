"""Gendiff."""

import os

from gendiff.reader_ext_source import data_parser
from gendiff.comparator import build_diff
from gendiff.formats.formatter import DEFAULT, format_diff


def _read_data_from_file(path_to_file: str) -> str:
    try:
        with open(path_to_file, 'r') as out:
            return out.read()
    except OSError as err:
        print('File not found: {0}'.format(err))


def _fetch_data_type(source: str) -> str:
    _, extension = os.path.splitext(source)
    extension = extension.lower()

    if extension == '.json':
        return 'json'
    elif extension in ('.yml', '.yaml'):  # noqa: WPS510
        return 'yml'
    return 'unknown'


def generate_diff(data1: str, data2: str, data_format=DEFAULT) -> str:
    """
    Generate diff for a given files.

    Parameters:
        data1: first data
        data2: second data
        data_format: output data format, default stylish

    Returns:
        return diff
    """
    first_data = data_parser(
        _read_data_from_file(data1),
        _fetch_data_type(data1),
    )
    second_data = data_parser(
        _read_data_from_file(data2),
        _fetch_data_type(data2),
    )

    diff = build_diff(first_data, second_data)

    return format_diff(diff, data_format)
