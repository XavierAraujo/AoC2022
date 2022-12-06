import re
from enum import Enum
from dataclasses import dataclass
from utils import print_answer
from utils import flatten_list
from tree import TreeNode

CHALLENGE_INPUT = "./resources/day7-input1.txt"


class Command(Enum):
    NONE = 0
    CD = 1
    LS = 2


class FileType(Enum):
    DIR = 0
    REGULAR = 1


@dataclass
class NodeData:
    file_type: FileType
    size: int


def challenge1():
    with open(CHALLENGE_INPUT, 'r') as f:
        root = parse_input_to_tree(f.read().splitlines())
    return get_size_sum_of_dir_node_below_size(root, 100000)


def challenge2():
    total_size = 70000000
    required_size = 30000000

    with open(CHALLENGE_INPUT, 'r') as f:
        root = parse_input_to_tree(f.read().splitlines())

    dir_nodes = get_all_dir_nodes(root)
    size_to_free = calcutate_size_to_free(total_size, get_node_size(root), required_size)
    min_size = total_size
    for dir_node in dir_nodes:
        node_size = get_node_size(dir_node)
        if size_to_free <= node_size < min_size:
            min_size = node_size
    return min_size


def parse_input_to_tree(lines: list[str]) -> TreeNode:
    root = TreeNode("/", None, NodeData(FileType.DIR, 0))
    current_node = root
    for line in lines[1:]:  # Starting on index 1 to ignore the 'cd' command to root
        cmd = get_command(line)
        if cmd == Command.CD:
            dirname = get_dirname_from_cd_command(line)
            if dirname == "..":
                current_node = current_node.parent
            else:
                current_node = current_node.append_child(dirname, NodeData(FileType.DIR, 0))
        elif cmd == Command.NONE and is_file_entry(line):
            # result of a previous ls command
            name, size = get_filename_and_size(line)
            current_node.append_child(name, NodeData(FileType.REGULAR, size))

    return root


def get_command(line: str):
    if line[0] != "$":
        return Command.NONE
    if line.strip() == "$ ls":
        return Command.LS
    return Command.CD


def get_dirname_from_cd_command(cmd):
    res = re.match(r"\$ cd ([A-Z-a-z0-9\.]*)", cmd)
    return res.group(1)


def is_file_entry(line):
    return re.match(r"([0-9]*) ([A-Z-a-z0-9\.]*)", line) is not None


def get_filename_and_size(line):
    res = re.match(r"([0-9]*) ([A-Z-a-z0-9\.]*)", line)
    return res.group(2), int(res.group(1))


def get_size_sum_of_dir_node_below_size(root, limit_size):
    accum_size = 0
    dir_nodes = get_all_dir_nodes(root)
    for dir_node in dir_nodes:
        dir_node_size = get_node_size(dir_node)
        if dir_node_size <= limit_size:
            accum_size += dir_node_size

    return accum_size


def get_all_dir_nodes(root: TreeNode) -> list[TreeNode]:
    dir_nodes = [[root]]
    for node in root.children:
        if node.data.file_type == FileType.DIR:
            dir_nodes.append(get_all_dir_nodes(node))
    return flatten_list(dir_nodes)


def get_node_size(node):
    return node.data.size + sum(get_node_size(c) for c in node.children)


def calcutate_size_to_free(total_size, used_size, required_size):
    free_size = total_size - used_size
    return required_size - free_size


if __name__ == '__main__':
    print_answer("challenge 1", challenge1)
    print_answer("challenge 2", challenge2)
