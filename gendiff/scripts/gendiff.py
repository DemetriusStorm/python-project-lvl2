"""
The package compares two files.

Outputs the result in the specified format.
"""


import argparse
import json
import os
from collections import defaultdict


def file_type_check(path_to_file):
    """
    Check file extension.

    Parameters:
        path_to_file: path to file

    Returns:
        return string ext
    """
    if os.path.isfile(path_to_file):
        filename = os.path.split(path_to_file)[1]
        extension = filename.split('.')[1]
    else:
        return 'File not found'
    return extension


def data_reception(path_to_file):
    """
    Load data from source.

    Parameters:
        path_to_file: path to file

    Returns:
        return dictionary
    """
    extensions = ['json', 'yaml', 'plane']
    ext = file_type_check(path_to_file)

    if ext not in extensions:
        return 'Error, file must be one from {0}'.format(extensions)

    with open(path_to_file, 'r') as datafile:
        return json.loads(datafile.read())


def convert_to_string(dictionary):
    """
    Convert dict to manual string.

    Parameters:
        dictionary: source dict

    Returns:
        return string
    """
    mapped = {
        'kept': '  ',
        'changed_old': ' -',
        'changed_new': ' +',
        'removed': ' -',
        'added': ' +',
    }
    empty = ''
    template = '{0} {1}\n'
    converted = ''.join(
        template.format(mapped[node], dictionary[node])
        for node in mapped if dictionary[node]
    ).replace('{', empty).replace('}', empty).replace("'", empty)
    return ''.join(['{\n', converted, '}'])


def generate_diff(first_file, second_file):
    """
    Given compares two files result in the specified format.

    Parameters:
        first_file: first source file
        second_file: second source file

    Returns:
        return string result difference files.
    """
    diff = defaultdict(dict)
    for key1, value1 in data_reception(first_file).items():
        if key1 in data_reception(second_file):
            if value1 == data_reception(second_file).get(key1, None):
                diff['kept'].update({key1: value1})
            else:
                diff['changed_old'].update({key1: value1})
                diff['changed_new'].update(
                    {
                        key1: data_reception(second_file).get(key1, None),
                    },
                )
        else:
            diff['removed'].update({key1: value1})

        for key2, value2 in data_reception(second_file).items():
            if key2 not in data_reception(first_file):
                diff['added'].update({key2: value2})
    return convert_to_string(diff)


def main():
    """Generate main function."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    result_diff = generate_diff(args.first_file, args.second_file)
    # TODO: will fix this later
    print('{0}'.format(result_diff))  # noqa: WPS421


if __name__ == '__main__':
    main()
