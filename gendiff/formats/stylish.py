"""Formatter stylish."""


def calculate_indent(depth, indent_size=4, indent_type=' '):
    """
    The indentation selector depending on the depth of the tree.

    Parameters:
        depth: tree depth.
        indent_size: indent size
        indent_type: indent type (separator)

    Returns:
        String of indent.
    """
    return indent_type * indent_size * depth


def format_diff(node, depth=0):  # noqa: WPS212
    """
    Format diff results as strings with indents.

    Parameters:
        node: tree node.
        depth: tree depth.

    Returns:
        String of diff rows, structured by indents.

    Raises:
        ValueError: When the unknown node type is given.
    """
    node_type = node['type']
    key = node.get('key')
    children = node.get('children')
    indent = calculate_indent(depth)

    if node_type == 'origin':
        calculate_rows = []
        for child in children:
            calculate_rows.append('{0}{1}\n'.format(
                indent,
                format_diff(child, depth),
            ))
        return '{{\n{0}}}'.format(''.join(calculate_rows))

    if node_type == 'nested':
        calculate_rows = []
        for child in children:
            calculate_rows.append('{0}\n'.format(
                format_diff(child, depth + 1),
            ))
        return '{0}    {1}: {{\n{2}{3}}}'.format(
            indent,
            key,
            ''.join(calculate_rows),
            calculate_indent(depth + 1),
        )

    if node_type == 'added':
        return '{0}  + {1}: {2}'.format(
            indent,
            key,
            _walk_string(node['value'], depth),
        )

    if node_type == 'removed':
        return '{0}  - {1}: {2}'.format(
            indent,
            key,
            _walk_string(node['value'], depth),
        )

    if node_type == 'updated':
        return '\n'.join([
            '{0}  - {1}: {2}'.format(
                indent,
                key,
                _walk_string(node['old_value'], depth),
            ),
            '{0}  + {1}: {2}'.format(
                indent,
                key,
                _walk_string(node['new_value'], depth),
            ),
        ])

    if node_type == 'unchanged':
        return '{0}    {1}: {2}'.format(
            indent,
            key,
            _walk_string(node['value'], depth),
        )

    raise ValueError('The specified node type is not detected')


def _walk_string(node, tree_depth):
    if node is None:
        return 'null'

    if isinstance(node, bool):
        return str(node).lower()

    elif isinstance(node, dict):
        result_string = []
        for key, node_value in node.items():
            result_string.append('{0}    {1}: {2}\n'.format(
                calculate_indent(tree_depth + 1),
                key,
                _walk_string(node_value, tree_depth + 1),
            ))

        return '{{\n{0}{1}}}'.format(
            ''.join(result_string),
            calculate_indent(tree_depth + 1),
        )
    return node
