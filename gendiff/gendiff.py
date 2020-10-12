"""Gedniff."""

KEYS_STATE = (
    UNCHANGED,
    REPLACED,
    ADDED,
    DELETED,
    NESTED,
) = (
    'unchanged',
    'replaced',
    'added',
    'deleted',
    'nested',
)


def gen_tree(data):
    """
    Build tree.

    Parameters:
        data: data

    Returns: tree
    """
    result = {}
    for key in data:
        if isinstance(data[key], dict):
            result[key] = (NESTED, gen_tree(data[key]))
        else:
            result[key] = (UNCHANGED, data[key])

    return result


def gen_state(state, value):
    """
    Check isinstance
    Parameters:
        state: state data
        value: data

    Returns: result (state, data) of data
    """
    # TODO: fix 'result = None'
    # result = None
    if isinstance(value, dict):
        result = state, gen_tree(value)
    else:
        result = state, value

    return result


def gen_diff(main_data, changed_data):
    """
    Build diff.

    Parameters:
        main_data: main_data
        changed_data: changed_data

    Returns: diff
    """

    diff = {}
    keys_state = {
        UNCHANGED: main_data.keys() & changed_data.keys(),
        DELETED: main_data.keys() - changed_data.keys(),
        ADDED: changed_data.keys() - main_data.keys()
    }

    for key, value in main_data.items():
        if key in keys_state[UNCHANGED]:
            common_key = changed_data[key]
            if isinstance(value, dict) and isinstance(
                    common_key,
                    dict):
                diff[key] = (NESTED, gen_diff(
                    value,
                    common_key))
            elif value == common_key:
                diff[key] = (UNCHANGED, value)
            else:
                # TODO: fix change to func?
                if isinstance(common_key, dict) and not isinstance(value,
                                                                   dict):
                    diff[key] = REPLACED, gen_tree(common_key), value
                elif not isinstance(common_key, dict) and isinstance(value,
                                                                     dict):
                    diff[key] = REPLACED, common_key, gen_tree(value)
                else:
                    diff[key] = REPLACED, common_key, value

        elif key in keys_state[DELETED]:
            diff[key] = gen_state(DELETED, value)

    for key, value in changed_data.items():
        if key in keys_state[ADDED]:
            diff[key] = gen_state(ADDED, value)

    return diff
