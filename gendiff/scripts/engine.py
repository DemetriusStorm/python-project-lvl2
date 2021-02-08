"""Engine."""

import argparse
from gendiff import parsers, formats, gendiff

# from gendiff.gendiff import args, format_diff, generate_diff

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


def main():
    """Generate result diff function."""

    args = parser.parse_args()
    if args.format == formats.JSON:
        format_diff = formats.render_json
    elif args.format == formats.PLAIN:
        format_diff = formats.render_plain
    elif args.format is None:
        format_diff = formats.render_simple
    else:
        raise Exception('Format is not supported.')

    first_file = parsers.get_data(args.first_file)
    second_file = parsers.get_data(args.second_file)
    print(format_diff(gendiff.generate_diff(first_file, second_file)))


if __name__ == '__main__':
    main()
