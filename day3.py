from utils import print_answer
from utils import chunks

CHALLENGE_INPUT = "./resources/day3-input1.txt"


def challenge1():
    priorities_sum = 0
    with open(CHALLENGE_INPUT, 'r') as f:
        for line in f.read().splitlines():
            rucksack1 = line[0:len(line)//2]
            rucksack2 = line[len(line)//2:]
            priorities_sum += calculate_repeated_item_priority([rucksack1, rucksack2])
    return priorities_sum


def challenge2():
    priorities_sum = 0
    with open(CHALLENGE_INPUT, 'r') as f:
        for lines in chunks(f.read().splitlines(), 3):
            priorities_sum += calculate_repeated_item_priority([lines[0], lines[1], lines[2]])
    return priorities_sum


def calculate_repeated_item_priority(rucksacks: list[str]):
    repeated_item = set.intersection(*[set(rucksack) for rucksack in rucksacks]).pop()
    return calculate_item_priority(repeated_item)


def calculate_item_priority(item):
    if 'a' <= item <= 'z':
        return ord(item) - (ord('a')) + 1  # Adjust ASCII value to item priority value of lower-case character items
    return ord(item) - (ord('A')) + 27  # Adjust ASCII value to item priority value of upper-case character items


if __name__ == '__main__':
    print_answer("challenge 1", challenge1)
    print_answer("challenge 2", challenge2)
