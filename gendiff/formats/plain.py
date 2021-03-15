"""Formatter plain."""

from gendiff.formats.plain_flat import flat_diff, make_string


def format_diff(diff):
    """
    Format diff results as a plain text.

    Parameters:
        diff: List with the diff result rows.

    Returns:
        String of diff rows, formatted as a plain text.
    """
    return make_string(flat_diff(diff))
