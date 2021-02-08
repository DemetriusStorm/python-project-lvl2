"""Read data from external sources."""

import json
import argparse

import yaml

EXTENSIONS = ('.json', '.yaml', '.yml')

parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument(
    'first_file',
    type=str,
    help='select first file to compare',
)
parser.add_argument(
    'second_file',
    type=str,
    help='select second file to compare',
)
parser.add_argument(
    '-f',
    '--format',
    type=str,
    help='set format of output',
)


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
