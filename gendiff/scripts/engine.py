"""Engine."""

import argparse

from gendiff import gendiff, parsers, formats  # noqa: I001


def main():
    """
    Generate result diff function.

    Raises:
        Exception: extension not in supported ext
    """
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
    args = parser.parse_args()
    if args.format == formats.JSON:
        format_diff = formats.json
    elif args.format == formats.PLAIN:
        format_diff = formats.plain
    elif args.format is None:
        format_diff = formats.simple
    else:
        raise Exception('Format is not supported.')

    first_file = parsers.get_data(args.first_file)
    second_file = parsers.get_data(args.second_file)

    diff = gendiff.gen_diff(first_file, second_file)
    # TODO: fix func(print) noqa: WPS421
    print(format_diff(diff))  # noqa: WPS421


if __name__ == '__main__':
    main()
