"""Test, test."""

import argparse
from gendiff import gendiff, parsers, formats

parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('first_file',
                    type=str,
                    help='select first file to compare')
parser.add_argument('second_file',
                    type=str,
                    help='select second file to compare')
parser.add_argument('-f', '--format',
                    type=str,
                    help='set format of output')


def catch_exceptions(func_object):
    """
    Decorator try catch exceptions.

    Parameters:
        func_object: any function

    Returns: result or except
    """
    def try_to_run():
        try:
            func_object()
        except Exception as e:
            print('Error:', str(e))

    return try_to_run


@catch_exceptions
def main():
    """Main function."""

    # TODO: fix WPS421 before production?
    args = parser.parse_args()
    # TODO: fix 'format_diff = None'
    # format_diff = None
    if args.format == formats.JSON:
        format_diff = formats.json
    elif args.format == formats.PLAIN:
        format_diff = formats.plain
    elif not args.format:
        format_diff = formats.simple
    else:
        raise Exception('Format is not supported.')

    first_file = parsers.get_data(args.first_file)
    second_file = parsers.get_data(args.second_file)

    diff = gendiff.build_diff(first_file, second_file)
    # TODO: fix func(print) noqa: WPS421
    print(format_diff(diff))  # noqa: WPS421


if __name__ == "__main__":
    main()
