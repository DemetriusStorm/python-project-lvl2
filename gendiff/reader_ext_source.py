"""Read data from external sources."""

import json

import yaml
import os


def result_parser(source):
    """
    Read files with a given file names and return list of files structure.

    Parameters:
        source: The path to the file to read.

    Raises:
        ValueError: if call to something fails.

    Returns:
        File content, parsed to the dictionary.
    """
    _, file_ext = os.path.splitext(source)
    file_ext = file_ext.lower()

    with open(source, 'r') as source_data:
        if file_ext == '.json':
            return json.load(source_data)
        elif file_ext in ('.yml', '.yaml'):  # noqa: WPS510
            return yaml.safe_load(source_data)
        raise ValueError('Unknown file format: {0}'.format(file_ext))
