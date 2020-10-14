"""Formatter json."""

import json


def render_json(diff):
    """
    Dump data to json.

    Parameters:
        diff: diff

    Returns:
        return dump diff
    """
    return json.dumps(diff)
