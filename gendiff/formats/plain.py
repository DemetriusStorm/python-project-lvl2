"""Formatter plain."""
from gendiff.gendiff import DELETED, ADDED, REPLACED, NESTED  # noqa: I001


def make_result(key, node_value, state, replaced_value=None):
    """
    Make text diff result.

    Parameters:
        key: key
        node_value: value
        state: state diff
        replaced_value: replaced_value

    Returns:
        return result diff
    """
    result_diff = ''

    if node_value is True:
        node_value = 'true'

    elif isinstance(node_value, dict):
        node_value = 'complex value'

    if state == DELETED:
        result_diff = "Property '{0}' removed".format(key)

    elif state == ADDED:
        result_diff = "Property '{0}' added with value: '{1}'".format(
            key,
            node_value,
        )

    elif state == REPLACED:
        if isinstance(replaced_value, dict):
            replaced_value = 'complex value'

        result_diff = "Property '{0}' changed, from '{1}' to '{2}'".format(
            key,
            replaced_value,
            node_value,
        )

    return '{0}{1}'.format(result_diff, '\n')


def render_diff(diff, root_key=None):
    """
    Render diff.

    Parameters:
        diff: diff
        root_key: root_key

    Returns:
        return rendered diff.
    """
    result_render = ''

    for key, node_value in diff.items():
        tree_items = '{0}.{1}'.format(root_key, key) if root_key else key

        if node_value[0] == NESTED:
            result_render += '{0}{1}'.format(
                render_diff(node_value[1], tree_items),
                '\n',
            )

        elif node_value[0] == REPLACED:
            result_render += make_result(
                tree_items,
                node_value[1],
                REPLACED,
                node_value[2],
            )

        elif node_value[0] in ADDED or node_value[0] in DELETED:
            result_render += make_result(
                tree_items,
                node_value[1],
                node_value[0],
            )

    return result_render.rstrip('\n')
