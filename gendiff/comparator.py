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
    collected_keys = _collect_keys(dict1, dict2)

    diff = []

    for key in collected_keys['all_keys']:
        diff_value1 = dict1.get(key, {})
        diff_value2 = dict2.get(key, {})
        if key in collected_keys['removed_keys']:
            diff.append(
                _gen_diff_row(
                    key,
                    data_compare(diff_value1, diff_value1) if isinstance(
                        diff_value1, dict,
                    ) else diff_value1,
                    'removed',
                ),
            )
        elif key in collected_keys['added_keys']:
            diff.append(
                _gen_diff_row(
                    key,
                    data_compare(diff_value2, diff_value2) if isinstance(
                        diff_value2, dict,
                    ) else diff_value2,
                    'added',
                ),
            )
        elif diff_value1 == diff_value2:
            diff.append(
                _gen_diff_row(
                    key,
                    data_compare(diff_value1, diff_value2) if isinstance(
                        diff_value1, dict,
                    ) else diff_value1,
                    'unmodified',
                ),
            )
        elif isinstance(diff_value1, dict) and isinstance(diff_value2, dict):
            diff.append(
                _gen_diff_row(
                    key,
                    data_compare(diff_value1, diff_value2),
                    'unmodified',
                ),
            )
        else:
            diff.append(
                _gen_diff_row(
                    key,
                    _gen_nested_diff(dict1, dict2, key),
                    'updated',
                ),
            )

    return diff


def _gen_diff_row(diff_key, diff_value, diff_state):
    return {
        'key': diff_key,
        'value': diff_value,
        'state': diff_state,
    }


def _gen_nested_diff(dict1, dict2, key):
    diff_value1 = dict1[key]
    diff_value2 = dict2[key]

    return {
        'old': data_compare(diff_value1, diff_value1)
        if isinstance(diff_value1, dict) else diff_value1,
        'new': data_compare(diff_value2, diff_value2)
        if isinstance(diff_value2, dict) else diff_value2,
    }


def _collect_keys(dict1, dict2):
    if dict1.keys() == dict2.keys():
        all_keys = dict1.keys()
    else:
        all_keys = list(dict1.keys() | dict2.keys())
        all_keys.sort()

    return {
        'all_keys': all_keys,
        'removed_keys': dict1.keys() - dict2.keys(),
        'added_keys': dict2.keys() - dict1.keys(),
    }
