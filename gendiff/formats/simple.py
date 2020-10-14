"""Formatter simple text."""

from gendiff.gendiff import UNCHANGED, DELETED, ADDED  # noqa: I001
from gendiff.gendiff import REPLACED, NESTED  # noqa: I001

render_sign = {
    UNCHANGED: None,
    ADDED: '+',
    DELETED: '-',
    NESTED: None,
}


def _bool(node_value, mutt):
    return isinstance(node_value, mutt)


def make_result(key, node_value, space, sign=None):
    """
    Make result.

    Parameters:
        key: key
        node_value: value
        space: spaces
        sign: sign

    Returns:
        return result line
    """
    string_space = '{0}{1}'.format('', (' ' * space))
    if not sign:
        sign = ' '

    if node_value is True:
        node_value = 'true'

    return '{0}{1} {2}: {3}\n'.format(
        string_space,
        sign,
        key,
        node_value,
    )


def render_diff(diff, space=2):  # noqa: WPS231
    """
    Convert to text format.

    Parameters:
        diff: diff
        space: spaces

    Returns:
        return rendered result.
    """
    plus = '+'
    minus = '-'
    tree = '{0}{1}'.format('{', '\n')

    for key, node in diff.items():
        if node[0] == NESTED:
            tree += make_result(
                key,
                render_diff(node[1], space=space + 4),
                space,
            )

        elif _bool(node[1], dict) and node[0] != REPLACED:
            tree += make_result(
                key,
                render_diff(node[1], space=space + 4),
                space,
                sign=render_sign[node[0]],
            )

        elif node[0] == REPLACED:
            if _bool(node[1], dict) and not _bool(node[2], dict):
                tree += make_result(
                    key,
                    render_diff(node[1], space=space + 4),
                    space=space,
                    sign=plus,
                )
                tree += make_result(key, node[2], space=space, sign=minus)

            elif not _bool(node[1], dict) and _bool(node[2], dict):
                tree += make_result(key, node[1], space=space, sign=plus)
                tree += make_result(
                    key,
                    render_diff(node[2], space=space + 4),
                    space=space,
                    sign=minus,
                )

            else:
                tree += make_result(key, node[1], space=space, sign=plus)
                tree += make_result(key, node[2], space=space, sign=minus)

        else:
            tree += make_result(
                key,
                node[1],
                space=space,
                sign=render_sign[node[0]],
            )

    tree += '{0}{1}'.format(' ' * (space - 2), '}')

    return tree
