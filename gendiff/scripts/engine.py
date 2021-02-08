"""Engine."""

from gendiff import parsers
from gendiff.gendiff import args, format_diff, generate_diff


def main():
    """Generate result diff function."""
    first_file = parsers.get_data(args.first_file)
    second_file = parsers.get_data(args.second_file)
    print(format_diff(generate_diff(first_file, second_file)))


if __name__ == '__main__':
    main()
