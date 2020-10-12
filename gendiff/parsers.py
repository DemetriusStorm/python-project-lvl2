"""Parsers."""

import os
import json
import yaml

EXTENSIONS = (
    JSON,
    YAML,
    YML,
) = (
    '.json',
    '.yaml',
    '.yml',
)


def result_parser(file_ext, source):
    """
    Result dump data from source.

    Parameters:
        file_ext: file extension
        source: source

    Returns: dump
    """
    with open(source, 'r') as f:
        if file_ext == JSON:
            return json.load(f)
        elif file_ext in (YAML, YML):
            return yaml.safe_load(f)


def get_data(source_file):
    """
    Load data from file.

    Parameters:
        source_file:

    Returns: data
    """
    file_ext = os.path.splitext(source_file)[1]
    if file_ext not in EXTENSIONS:
        raise Exception('Format {file_ext} is not supported.'.format(
            file_ext=file_ext,
        ))
    else:
        return result_parser(file_ext, source_file)
