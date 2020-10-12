"""Plain formatter."""

from gendiff.gendiff import DELETED, ADDED, REPLACED, NESTED


def make_result(key, value, state, replaced_value=None):
    """
    Making result.

    Parameters:
        key: key
        value: value
        state: state
        replaced_value:
    """

    result = ''
    if value is True:
        value = 'true'

    elif isinstance(value, dict):
        value = 'complex value'

    if state == DELETED:
        result = 'Property \'{key}\' removed'.format(key=key)

    elif state == ADDED:
        result = 'Property \'{key}\' added with value: \'{value}\''.format(
            key=key, value=value
        )

    elif state == REPLACED:
        if isinstance(replaced_value, dict):
            replaced_value = 'complex value'
        result = 'Property \'{key}\' changed, from \'{old_value}\' ' \
                 'to \'{new_value}\''.format(key=key,
                                             old_value=replaced_value,
                                             new_value=value)

    return result + '\n'


def render_diff(diff, root_key=None):
    """
    Render diff.

    Parameters:
        diff: diff
        root_key: root_key

    Returns: rendered diff.
    """
    result = ''

    for key, value in diff.items():
        tree_items = '{root}.{key}'.format(root=root_key, key=key) \
            if root_key else key

        if value[0] == NESTED:
            result += render_diff(
                value[1],
                tree_items
            ) + '\n'

        elif value[0] == REPLACED:
            result += make_result(
                tree_items,
                value[1],
                REPLACED,
                value[2],
            )

        elif value[0] in (ADDED, DELETED):
            result += make_result(
                tree_items,
                value[1],
                value[0],
            )

    return result.rstrip('\n')
