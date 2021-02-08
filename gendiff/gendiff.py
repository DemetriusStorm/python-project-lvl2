"""Gendiff."""

import argparse

from gendiff import formats

UNCHANGED, REPLACED, ADDED = 'unchanged', 'replaced', 'added'
DELETED, NESTED = 'deleted', 'nested'

parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument(
    'first_file',
    type=str,
    help='select first file to compare',
)
parser.add_argument(
    'second_file',
    type=str,
    help='select second file to compare',
)
parser.add_argument(
    '-f',
    '--format',
    type=str,
    help='set format of output',
)

args = parser.parse_args()
if args.format == formats.JSON:
    format_diff = formats.json
elif args.format == formats.PLAIN:
    format_diff = formats.plain
elif args.format is None:
    format_diff = formats.simple
else:
    raise Exception('Format is not supported.')


def gen_tree(nodes):
    """
    Build tree.

    Parameters:
        nodes: nodes

    Returns:
        return result tree
    """
    tree = {}
    for key, _ in nodes.items():
        if isinstance(nodes[key], dict):
            tree[key] = (NESTED, gen_tree(nodes[key]))
        else:
            tree[key] = (UNCHANGED, nodes[key])

    return tree


def gen_state(state, node):
    """
    Check isinstance.

    Parameters:
        state: state data
        node: node

    Returns:
        return result (state, data) of data
    """
    if isinstance(node, dict):
        tree = state, gen_tree(node)
    else:
        tree = state, node

    return tree


def gen_diff(main_data, changed_data):  # noqa: WPS210
    """
    Build diff.

    Parameters:
        main_data: main_data
        changed_data: changed_data

    Returns:
        return diff
    """
    diff = {}
    keys_state = {
        UNCHANGED: main_data.keys() & changed_data.keys(),
        DELETED: main_data.keys() - changed_data.keys(),
        ADDED: changed_data.keys() - main_data.keys(),
    }

    for key, node in main_data.items():
        if key in keys_state[UNCHANGED]:
            shared = changed_data[key]
            if isinstance(node, dict) and isinstance(shared, dict):
                diff[key] = (NESTED, gen_diff(node, shared))
            elif node == shared:
                diff[key] = (UNCHANGED, node)
            else:
                if isinstance(shared, dict) and not isinstance(node, dict):
                    diff[key] = REPLACED, gen_tree(shared), node
                elif not isinstance(shared, dict) and isinstance(node, dict):
                    diff[key] = REPLACED, shared, gen_tree(node)
                else:
                    diff[key] = REPLACED, shared, node

        elif key in keys_state[DELETED]:
            diff[key] = gen_state(DELETED, node)

    for key_after, value_after in changed_data.items():
        if key_after in keys_state[ADDED]:
            diff[key_after] = gen_state(ADDED, value_after)

    return diff
