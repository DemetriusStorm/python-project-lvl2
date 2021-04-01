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
    return json.dumps(diff)
