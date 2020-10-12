"""Json formatter"""

import json


def render_json(diff):
    """
    Dumping data to json

    Parameters:
        diff: diff

    Returns: dump diff
    """
    return json.dumps(diff)
