"""Gendiff."""

from gendiff.reader_ext_source import result_parser
from gendiff.comparator import data_compare
from gendiff.formats.formatter import DEFAULT, format_diff


def generate_diff(main_data, changed_data, file_format=DEFAULT):
    """
    Generate diff for a given files.

    Parameters:
        main_data: first file
        changed_data: second file
        file_format: output file format, default stylish

    Returns:
        return diff
    """
    before_data = result_parser(main_data)
    after_data = result_parser(changed_data)
    diff = data_compare(before_data, after_data)

    return format_diff(diff, file_format)
