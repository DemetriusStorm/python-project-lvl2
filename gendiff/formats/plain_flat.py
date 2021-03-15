"""Formatter plain."""

COMPLEX_VALUE = '[complex value]'

STATE_ADDED = 'added'
STATE_REMOVED = 'removed'
STATE_UNMODIFIED = 'unmodified'
STATE_UPDATED = 'updated'


def _format_value(row_value):
    if row_value == '[complex value]':
        return row_value
    if row_value is None:
        return 'null'
    if isinstance(row_value, bool):
        return str(row_value).lower()

    if isinstance(row_value, int):
        return row_value

    return "'{0}'".format(row_value)


def _flat_added_row(row, complex_key):
    row_value = row['value']
    row_state = row['state']

    return (
        complex_key,
        COMPLEX_VALUE if isinstance(row_value, list) else row_value,
        row_state,
    )


def _flat_updated_row(row, complex_key):
    values_pair = row['value']

    if isinstance(values_pair['old'], list):
        values_pair['old'] = COMPLEX_VALUE

    if isinstance(values_pair['new'], list):
        values_pair['new'] = COMPLEX_VALUE

    return complex_key, values_pair, row['state']


def make_string(diff):
    """
    Format diff results row.

    Parameters:
        diff: List with the diff result rows.

    Returns:
        Formatted string row.
    """
    string_rows = []
    for row in diff:
        state = row[-1]
        if state == STATE_ADDED:
            string_rows.append(
                "Property '{0}' was added with value: {1}".format(
                    row[0],
                    _format_value(row[1]),
                ))
        elif state == STATE_UPDATED:
            string_rows.append(
                "Property '{0}' was updated. From {1} to {2}".format(
                    row[0],
                    _format_value(row[1]['old']),
                    _format_value(row[1]['new']),
                ))
        elif state == STATE_REMOVED:
            string_rows.append(
                "Property '{0}' was removed".format(
                    row[0],
                ))

    return '\n'.join(string_rows)


def flat_diff(diff, parent_key='', sep='.'):
    """
    Format flatten diff.

    Parameters:
        diff: List with the diff result rows.
        parent_key: parent key
        sep: separator

    Returns:
        Flatten items.
    """
    flat_items = []
    for row in diff:
        row_state = row['state']
        row_value = row['value']
        new_key = '{0}{1}{2}'.format(
            parent_key,
            sep,
            row['key'],
        ) if parent_key else row['key']

        if row_state == 'removed':
            flat_items.append((new_key, row_state))
        elif row_state == STATE_ADDED:
            flat_items.append(_flat_added_row(row, new_key))
        elif row_state == STATE_UNMODIFIED and isinstance(row_value, list):
            flat_items.extend(flat_diff(row_value, new_key, sep=sep))
        elif row_state == STATE_UPDATED:
            flat_items.append(_flat_updated_row(row, new_key))

    return flat_items
