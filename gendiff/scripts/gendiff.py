"""Engine."""

import argparse

from gendiff import generate_diff
from gendiff.formats.formatter import FORMATS, DEFAULT


def main():
    """Launch cli."""
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
        choices=FORMATS,
        default=DEFAULT,
        type=str,
        help='set format of output',
    )

    args = parser.parse_args()
    output_format = args.format

    try:
        diff = generate_diff(
            args.first_file,
            args.second_file,
            data_format=output_format,
        )
    except ValueError as ex:
        raise ValueError('Something happened... {0}'.format(ex))

    print(diff)


if __name__ == '__main__':
    main()
