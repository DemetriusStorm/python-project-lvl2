"""Read data from external sources."""

import json

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
