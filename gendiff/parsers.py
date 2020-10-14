"""Parsers."""

import json
import os

import yaml

EXTENSIONS = ('.json', '.yaml', '.yml')


def result_parser(file_ext, source):
    """
    Get result dump data from source.

    Parameters:
        file_ext: file extension
        source: source

    Returns:
        return object
    """
    with open(source, 'r') as source_data:
        if file_ext == '.json':
            return json.load(source_data)
        elif file_ext in EXTENSIONS:
            return yaml.safe_load(source_data)


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
    if ext in EXTENSIONS:
        return result_parser(ext, source_file)
    raise Exception('Format {0} is not supported.'.format(ext))
