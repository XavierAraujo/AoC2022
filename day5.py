import re
import itertools
from utils import print_answer
from dataclasses import dataclass

CHALLENGE_INPUT = "./resources/day5-input1.txt"


@dataclass
class Item:
    type: str
    stack: int


@dataclass
class Operation:
    n_items: int
    origin: int
    destination: int


def challenge1():
    items, operations = parse_input()
    stacks = input_items_to_stacks(items)
    do_operations_crate_mover_9000(stacks, operations)
    return ''.join([stack.pop() for stack in stacks])


def challenge2():
    items, operations = parse_input()
    stacks = input_items_to_stacks(items)
    do_operations_crate_mover_9001(stacks, operations)
    return ''.join([stack.pop() for stack in stacks])


def parse_input() -> (list[Item], list[Operation]):
    items = list()
    operations = list()
    with open(CHALLENGE_INPUT, 'r') as f:
        for line in f.read().splitlines():
            if line.find("[") != -1:
                items.append(parse_items(line))
            elif line.find("move") != -1:
                operations.append(parse_operation(line))
    return items, operations


def input_items_to_stacks(line_items):
    # Initializes all the required stacks assuming that there are no empty stacks
    stacks = [[] for _ in range(len(max(line_items, key=len)))]
    items = list(itertools.chain(*line_items))  # flatten list of list
    for item in reversed(items):  # The input items must be inserted in the reverse order
        stacks[item.stack - 1].append(item.type)
    return stacks


def parse_items(line):
    items = re.finditer(r'([A-Z])', line)
    return [Item(item.group(), item_position_to_stack_id(int(item.start(1)))) for item in items]


def item_position_to_stack_id(item_pos):
    # The item position based on the stack ID is given by:
    #   item_pos = 1 + (stack-id - 1) * 4
    return int((item_pos - 1) / 4 + 1)


def parse_operation(line):
    res = re.match(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)", line)
    n_items, origin, destination = int(res.group(1)), int(res.group(2)), int(res.group(3))
    return Operation(n_items, origin, destination)


def do_operations_crate_mover_9000(stacks, operations):
    for op in operations:
        for i in range(op.n_items):
            stacks[op.destination-1].append(stacks[op.origin-1].pop())


def do_operations_crate_mover_9001(stacks, operations):
    for op in operations:
        item_types_to_move = []
        for i in range(op.n_items):
            item_types_to_move.append(stacks[op.origin - 1].pop())
        for item_type in reversed(item_types_to_move):
            stacks[op.destination-1].append(item_type)


if __name__ == '__main__':
    print_answer("challenge 1", challenge1)
    print_answer("challenge 2", challenge2)
