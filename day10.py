import re
from utils import print_answer
from utils import chunks
from utils import time_measure
from abc import ABC, abstractmethod


CHALLENGE_INPUT = "./resources/day10-input1.txt"


class Operation(ABC):
    @abstractmethod
    def get_number_of_cycles(self):
        pass


class Noop(Operation):
    def get_number_of_cycles(self):
        return 1


class Addx(Operation):
    def __init__(self, value: int):
        self.value = value

    def get_number_of_cycles(self):
        return 2


def challenge1():
    with open(CHALLENGE_INPUT, 'r') as f:
        ops = parse_operations(f.read().splitlines())
    value_in_cycles = get_value_in_cycles(ops)
    return sum([i*value_in_cycles[i-1] for i in (20, 60, 100, 140, 180, 220)])


def challenge2():
    with open(CHALLENGE_INPUT, 'r') as f:
        ops = parse_operations(f.read().splitlines())
    return crt_get_lines(get_value_in_cycles(ops))


def crt_get_lines(value_in_cycles):
    return [crt_get_line(chunk) for chunk in chunks(value_in_cycles, 40)]


def crt_get_line(values):
    line = list()
    for i in range(len(values)):
        sprite_positions = range(values[i]-1, values[i]+2)
        if i in sprite_positions:
            line.append("#")
        else:
            line.append(".")
    return line


def get_value_in_cycles(operations):
    x_value = 1
    value_in_cycles = list()
    for op in operations:
        for i in range(op.get_number_of_cycles()):
            value_in_cycles.append(x_value)
        if isinstance(op, Addx):
            x_value += op.value
    return value_in_cycles


def parse_operations(lines):
    return [parse_operation(line) for line in lines]


def parse_operation(line):
    if line.find("addx") != - 1:
        res = re.match(r"addx ([\-0-9]+)", line)
        return Addx(int(res.group(1)))
    if line.find("noop") != - 1:
        return Noop()
    raise Exception("Invalid operation")


if __name__ == '__main__':
    print_answer("challenge 1", challenge1)

    crt_lines, elapsed_time = time_measure(challenge2)
    print(f"challenge 2 (took {elapsed_time} seconds): ")
    for crt_line in crt_lines:
        print(crt_line)
