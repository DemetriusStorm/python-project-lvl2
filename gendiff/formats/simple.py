"""Test, test."""

from gendiff.gendiff import UNCHANGED, DELETED, ADDED, REPLACED, NESTED

RENDER_SIGNS = {
    UNCHANGED: None,
    ADDED: '+',
    DELETED: '-',
    NESTED: None
}


def make_result(key, value, spaces, sign=None):
    """
    Make result.

    Parameters:
        key: key
        value: value
        spaces: spaces
        sign: sign

    Returns: result line
    """
    string_spaces = '' + (' ' * spaces)
    if not sign:
        sign = ' '

    if value is True:
        value = 'true'

    result = '{string_spaces}{sign} {key}: {value}\n'.format(
        string_spaces=string_spaces,
        sign=sign,
        key=key,
        value=value,
    )
    return result


def render_diff(diff, spaces=2):
    """
    Convert to text format.

    Parameters:
        diff: diff
        spaces: spaces

    Returns: rendered result.
    """
    result = '{' + '\n'

    for key, value in diff.items():
        if value[0] == NESTED:
            result += make_result(key,
                                  render_diff(value[1], spaces=spaces + 4),
                                  spaces)

        elif isinstance(value[1], dict) and not value[0] == REPLACED:
            result += make_result(key,
                                  render_diff(value[1], spaces=spaces + 4),
                                  spaces, sign=RENDER_SIGNS[value[0]])

        elif value[0] == REPLACED:
            if isinstance(value[1], dict) and not isinstance(value[2], dict):
                result += make_result(key,
                                      render_diff(value[1], spaces=spaces + 4),
                                      spaces=spaces, sign='+')
                result += make_result(key, value[2], spaces=spaces, sign='-')
            elif not isinstance(value[1], dict) and isinstance(value[2], dict):
                result += make_result(key, value[1], spaces=spaces, sign='+')
                result += make_result(key,
                                      render_diff(value[2], spaces=spaces + 4),
                                      spaces=spaces, sign='-')
            else:
                result += make_result(key, value[1], spaces=spaces, sign='+')
                result += make_result(key, value[2], spaces=spaces, sign='-')

        else:
            result += make_result(key, value[1], spaces=spaces,
                                  sign=RENDER_SIGNS[value[0]])

    result += ' ' * (spaces - 2) + '}'

    return result
