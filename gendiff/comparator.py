"""Gendiff."""


def data_compare(dict1, dict2):
    """
    Generate diff for a given dictionaries.

    Parameters:
        dict1: The first dictionary to compare.
        dict2: The second dictionary to compare.

    Returns:
        Diff of the given dictionaries.
    """
    all_keys = list(dict1.keys() | dict2.keys())
    diff = []

    for key in sorted(all_keys):
        if key not in dict1:
            diff.append(
                {
                    'type': 'added',
                    'key': key,
                    'value': dict2[key],
                },
            )
            continue

        if key not in dict2:
            diff.append(
                {
                    'type': 'removed',
                    'key': key,
                    'value': dict1[key],
                },
            )
            continue

        if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            diff.append(
                {
                    'type': 'nested',
                    'key': key,
                    'children': data_compare(dict1[key], dict2[key]),
                },
            )
            continue

        if dict1[key] != dict2[key]:
            diff.append(
                {
                    'type': 'updated',
                    'key': key,
                    'old_value': dict1[key],
                    'new_value': dict2[key],
                },
            )
            continue

        diff.append(
            {
                'type': 'unchanged',
                'key': key,
                'value': dict1[key],
            },
        )

    return diff


def build_diff(first_object: dict, second_object: dict) -> dict:
    """
    The function compares two objects.

    Args:
        first_object: first object.
        second_object: second object.

    Returns:
        Dictionary with the result of comparison.
    """
    return {
        'type': 'origin',
        'children': data_compare(first_object, second_object),
    }
