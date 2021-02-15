"""Engine."""

from gendiff import reader_ext_source, parsers, formats
from gendiff.gendiff import generate_diff

args = reader_ext_source.parser.parse_args()

if args.format == formats.JSON:
    format_diff = formats.render_json
elif args.format == formats.PLAIN:
    format_diff = formats.render_plain
elif args.format is None:
    format_diff = formats.render_simple
else:
    raise Exception('Format is not supported.')


def main():
    """Generate result diff function."""
    first_file = parsers.get_data(args.first_file)
    second_file = parsers.get_data(args.second_file)
    print(format_diff(generate_diff(first_file, second_file)))


if __name__ == '__main__':
    main()
