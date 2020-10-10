"""
The package compares two files.

Outputs the result in the specified format.
"""

import argparse
import json
import os
from collections import defaultdict

EXTENSIONS = ('json', 'yaml', 'plane')


def is_file(path_to_file: str) -> bool:
    """
    Check file in path.

    Parameters:
        path_to_file: path to file

    Returns:
        return bool
    """
    return os.path.isfile(path_to_file)


def check_extension(path_to_file: str) -> str:
    """
    Check file extension.

    Parameters:
        path_to_file: path to file

    Returns:
        return string
    """
    # TODO: will fix WPS421 before production
    # Check extension
    try:
        is_file(path_to_file)
    except FileExistsError as file_exist_error:
        print('File not found: {0}'.format(file_exist_error))  # noqa: WPS421

    # TODO: Check extension file - why? May be check data structure?
    filename = os.path.split(path_to_file)[1]
    if len(filename) < 2:
        print('File {0} without extension'.format(  # noqa: WPS421
            filename,
        ))
    else:
        ext = filename.split('.')[1]
        if ext not in EXTENSIONS:
            print('Error, file must be one of {0}'.format(  # noqa: WPS421
                EXTENSIONS,
            ))
        return ext


def data_reception(path_to_file: str) -> dict:
    """
    Load data from source.

    Parameters:
        path_to_file: path to file

    Returns:
        return dictionary
    """
    # TODO: will fix WPS421 before production
    try:
        with open(path_to_file, 'r') as json_read:
            json_data = json_read.read()
            data_out = json.loads(json_data)
    except TypeError:
        print('File {0} is not json'.format(  # noqa: WPS421
            path_to_file,
        ))
    return data_out


def convert_to_string(dictionary: dict) -> str:
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
    # TODO: will fix WPS421 before production
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    result_diff = generate_diff(args.first_file, args.second_file)
    print('{0}'.format(result_diff))  # noqa: WPS421


if __name__ == '__main__':
    main()
