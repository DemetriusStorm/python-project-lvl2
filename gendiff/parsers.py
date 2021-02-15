"""Parsers."""

import os

from gendiff import reader_ext_source


def get_data(source_file):
    """
    Load data from file.

    Parameters:
        source_file: source_file

    Returns:
        return data from result parser

    Raises:
        Exception: extension not in supported ext
    """
    ext = os.path.splitext(source_file)[1]
    if ext in reader_ext_source.EXTENSIONS:
        return reader_ext_source.result_parser(ext, source_file)
    raise Exception('Format {0} is not supported.'.format(ext))
