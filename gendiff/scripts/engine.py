"""Engine."""

from gendiff import gendiff, parsers
from gendiff.gendiff import args, format_diff


def main():
    """Generate result diff function."""
    first_file = parsers.get_data(args.first_file)
    second_file = parsers.get_data(args.second_file)

    diff = gendiff.gen_diff(first_file, second_file)
    print(format_diff(diff))


if __name__ == '__main__':
    main()
