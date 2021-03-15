"""Formatter stylish."""
import types

STATES = types.MappingProxyType({
    'added': '+',
    'removed': '-',
    'updated': ' ',
    'unmodified': ' ',
})


def format_diff(diff):
    """
    Format diff results as strings with indents.

    Parameters:
        diff: List with the diff result rows.

    Returns:
        String of diff rows, structured by indents.
    """
    return '{{\n{0}}}'.format(_convert_to_json_string(_stylish(diff)))


def _stylish(diff, indent=2):
    strings = []
    for row in diff:
        strings.append(_stylish_row(row, indent))
    return ''.join(strings)


def _stylish_row(row, indent):
    spaces = ' ' * indent

    row_key = row['key']
    row_value = row['value']
    row_state = row['state']

    if row_state == 'updated':
        string = _stylish_row(
            {
                'key': row_key,
                'value': row_value['old'],
                'state': 'removed',
            },
            indent,
        )
        string += _stylish_row(
            {
                'key': row_key,
                'value': row_value['new'],
                'state': 'added',
            },
            indent,
        )
        return string
    elif isinstance(row_value, list):
        string = '{0}{1} {2}: {{\n'.format(
            spaces, STATES[row_state], row_key,
        )
        string += _stylish(row_value, indent + 4)
        string += '{0}  }}\n'.format(spaces)
        return string

    return '{0}{1} {2}: {3}\n'.format(
        spaces, STATES[row_state], row_key, row_value,
    )


def _convert_to_json_string(string):
    return string.replace(
        'True',
        'true',
    ).replace(
        'False',
        'false',
    ).replace(
        'None',
        'null',
    )
