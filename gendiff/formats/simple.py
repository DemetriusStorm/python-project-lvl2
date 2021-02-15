"""Formatter simple text."""

from gendiff.gendiff import (
    UNCHANGED,
    REPLACED,
    ADDED,
    DELETED,
    NESTED,
)

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

    return '{0}{1} {2}: {3}'.format(
        string_space,
        sign,
        key,
        node_value,
    )


def render_diff(diff, space=2):
    """
    Convert to text format.

    Parameters:
        diff: diff
        space: spaces

    Returns:
        return rendered result.
    """
    tree = ['{']
    for key, node in diff.items():
        status, is_complex = node[0], node[1]
        if status == NESTED:
            tree.append(make_result(
                key,
                render_diff(is_complex, space=space + 4),
                space,
            ))

        elif _bool(is_complex, dict) and status != REPLACED:
            tree.append(make_result(
                key,
                render_diff(is_complex, space=space + 4),
                space,
                sign=render_sign[status],
            ))

        elif status == REPLACED:
            difference = (node[1], node[2])
            (new_value, old_value) = difference
            if _bool(new_value, dict) and not _bool(old_value, dict):
                tree.append(make_result(
                    key,
                    render_diff(new_value, space=space + 4),
                    space=space,
                    sign=render_sign[ADDED],
                ))
                tree.append(make_result(
                    key,
                    old_value,
                    space=space,
                    sign=render_sign[DELETED],
                ))

            elif not _bool(new_value, dict) and _bool(old_value, dict):
                tree.append(make_result(
                    key,
                    new_value,
                    space=space,
                    sign=render_sign[ADDED],
                ))
                tree.append(make_result(
                    key,
                    render_diff(old_value, space=space + 4),
                    space=space,
                    sign=render_sign[DELETED],
                ))

            else:
                tree.append(make_result(
                    key,
                    new_value,
                    space=space,
                    sign=render_sign[ADDED],
                ))
                tree.append(make_result(
                    key,
                    old_value,
                    space=space,
                    sign=render_sign[DELETED],
                ))

        else:
            tree.append(make_result(
                key,
                is_complex,
                space=space,
                sign=render_sign[status],
            ))

    tree.append('}')
    return '\n'.join(tree)
