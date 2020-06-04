"""
The package compares two files,
and outputs the result in the specified format.
"""

import argparse


def generate_diff(first_file='', second_file='', format_file='json'):
    """
    receive two position arguments (/path/to/file1, /path/to/file2)
    and out file format (-f [json []])

    :param first_file:
    :param second_file:
    :param format_file:
    :return: string result difference files
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    return parser.parse_args()


if __name__ == '__main__':
    generate_diff()
