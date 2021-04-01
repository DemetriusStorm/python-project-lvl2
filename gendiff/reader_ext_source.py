"""Read data from external sources."""
import json

import yaml


def data_parser(parsing_data: str, format_data: str) -> dict:
    """
    Read files with a given file names and return list of files structure.

    Parameters:
        parsing_data: data source.
        format_data: type of data, json or yml

    Raises:
        ValueError: if call to something fails.

    Returns:
        File content, parsed to the dictionary.
    """
    if format_data == 'json':
        return json.loads(parsing_data)
    elif format_data in ('yml', 'yaml'):  # noqa: WPS510
        return yaml.safe_load(parsing_data)

    raise ValueError('Unknown file format: {0}'.format(format_data))
