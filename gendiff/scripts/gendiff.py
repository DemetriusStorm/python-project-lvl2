"""
The package compares two files
and outputs the result in the specified format.
"""

import argparse

parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', help='set format of output')
args = parser.parse_args()


def main(name='Dima'):
    """Welcome function."""
    print(f'Welcome to Gendiff, {name}!')


if __name__ == '__main__':
    main()
