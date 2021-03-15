"""Formatter json."""
import json


def format_diff(diff):
    """
    Format diff results as a json.

    Parameters:
        diff: List with the diff result rows.

    Returns:
        String of diff rows, formatted as a json.
    """
    return json.dumps(_format_diff(diff))


def _format_diff(diff):
    json_diff = {}

    for row in diff:
        json_diff.update(
            {
                row['key']: {
                    'value': _format_value(row['value']),
                    'state': row['state'],
                },
            },
        )

    return json_diff


def _format_value(diff_value):
    if isinstance(diff_value, list):
        return _format_diff(diff_value)
    if isinstance(diff_value, dict):
        return {
            'old': _format_value(diff_value['old']),
            'new': _format_value(diff_value['new']),
        }
    return diff_value
