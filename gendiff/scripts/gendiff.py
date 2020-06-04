"""
The package compares two files.

Outputs the result in the specified format.
"""

import argparse


def generate_diff(first_file='', second_file='', format_file='json'):
    """
    Given compares two files result in the specified format.

    Parameters:
        first_file: first file /path/to/file1
        second_file: second file /path/to/file2
        format_file: format file output -f [json []]

    Returns:
        return string result difference files.
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    return parser.parse_args()


if __name__ == '__main__':
    generate_diff()
