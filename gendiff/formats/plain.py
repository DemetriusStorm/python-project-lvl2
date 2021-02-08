"""Formatter plain."""
from gendiff import DELETED, ADDED, REPLACED, NESTED


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
    elif node_value is False:
        node_value = 'false'
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

    return '{0}'.format(result_diff)


def render_diff(diff, root_key=None):
    """
    Render diff.

    Parameters:
        diff: diff
        root_key: root_key

    Returns:
        return rendered diff.
    """
    result_render = []

    for key, node_value in diff.items():
        status = node_value[0]
        is_complex = node_value[1]
        tree_items = '{0}.{1}'.format(root_key, key) if root_key else key

        if status == NESTED:
            result_render.append(render_diff(is_complex, tree_items))

        elif status == REPLACED:
            difference = (node_value[1], node_value[2])
            (new_value, old_value) = difference
            result_render.append(make_result(
                tree_items,
                new_value,
                REPLACED,
                old_value,
            ))

        elif status in ADDED or status in DELETED:
            result_render.append(make_result(
                tree_items,
                is_complex,
                status,
            ))
    print(result_render)
    return '\n'.join(result_render)
