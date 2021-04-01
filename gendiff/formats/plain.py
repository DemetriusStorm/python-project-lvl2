"""Formatter plain."""


def _format_value(row_value):
    if isinstance(row_value, dict):
        return '[complex value]'
    elif row_value is None:
        return 'null'
    elif isinstance(row_value, str):
        return "'{0}'".format(row_value)

    return str(row_value).lower()


def _flat_list(node_items):
    flatten_rows = []
    if not isinstance(node_items, list):
        return [node_items]

    for node_value in node_items:
        flatten_rows.extend(_flat_list(node_value))

    return flatten_rows


def format_diff(node):  # noqa: WPS212
    """
    Format diff results as a plain text.

    Parameters:
        node: List with the diff result rows.

    Returns:
        String of diff rows, formatted as a plain text.

    Raises:
        ValueError: When the unknown node type is given
    """
    node_type = node['type']
    key = node.get('key')

    if node_type == 'origin':
        rows = [format_diff(child) for child in node.get('children')]
        return '\n'.join(_flat_list(rows))

    if node_type == 'nested':
        rows = []
        for child in node.get('children'):
            child['key'] = '{0}.{1}'.format(key, child['key'])
            rows.append(format_diff(child))
        return rows

    if node_type == 'added':
        return "Property '{0}' was added with value: {1}".format(
            key,
            _format_value(node['value']),
        )

    if node_type == 'removed':
        return "Property '{0}' was removed".format(key)

    if node_type == 'updated':
        return "Property '{0}' was updated. From {1} to {2}".format(
            key,
            _format_value(node['old_value']),
            _format_value(node['new_value']),
        )

    if node_type == 'unchanged':
        return []

    raise ValueError('There is no such node type')
