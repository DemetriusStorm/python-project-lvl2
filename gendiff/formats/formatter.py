"""Formatters."""

from gendiff.formats import json, plain, stylish

DEFAULT = 'stylish'

FORMATS = ('stylish', 'plain', 'json')


def format_diff(diff, style=DEFAULT):
    """
    Format the diff output with a given format style.

    Parameters:
        diff: A files structures compare result.
        style: A formatter name to format a diff.

    Returns:
        A formatted diff.

    Raises:
        ValueError: When the unknown format key is given.
    """
    if style in FORMATS:
        if style == 'plain':
            return plain.format_diff(diff)

        elif style == 'stylish':
            return stylish.format_diff(diff)

        elif style == 'json':
            return json.format_diff(diff)

    raise ValueError('Unknown diff output format!')
