"""First file used argparse and it module."""

import argparse

parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')
args = parser.parse_args()


def main(name='Dima'):
    """Welcome function."""
    print(f'Welcome to Gendiff, {name}!')


if __name__ == '__main__':
    main()
