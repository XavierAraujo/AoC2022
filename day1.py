import heapq
from utils import print_answer

CHALLENGE_INPUT = "./resources/day1-input1.txt"
CHALLENGE_2_N_ELFS = 3


def challenge2_nlogn():
    calories_by_elf = list()
    current_elf_calories = 0
    with open(CHALLENGE_INPUT, 'r') as f:
        for line in f.read().splitlines():
            if is_current_elf_count_finished(line):
                calories_by_elf.append(current_elf_calories)
                current_elf_calories = 0
                continue
            current_elf_calories += int(line)
    calories_by_elf.sort()
    calories_by_elf.reverse()
    return sum(calories_by_elf[0:CHALLENGE_2_N_ELFS])


def challenge2_logn():
    calories_heap = []
    current_elf_calories = 0
    with open(CHALLENGE_INPUT, 'r') as f:
        for line in f.read().splitlines():
            if is_current_elf_count_finished(line):
                heapq.heappush(calories_heap, - current_elf_calories)  # this is a min heap and we want a max heap so we invert the values
                current_elf_calories = 0
                continue
            current_elf_calories += int(line)

    return abs(sum([heapq.heappop(calories_heap) for _ in range(0, CHALLENGE_2_N_ELFS)]))  # Using abs() to invert back the heap values


def challenge1():
    max_elf_calories = 0
    current_elf_calories = 0
    with open(CHALLENGE_INPUT, 'r') as f:
        for line in f.read().splitlines():
            if is_current_elf_count_finished(line):
                if current_elf_calories > max_elf_calories:
                    max_elf_calories = current_elf_calories
                current_elf_calories = 0
                continue
            current_elf_calories += int(line)
    return max_elf_calories


def is_current_elf_count_finished(line):
    return len(line) == 0


if __name__ == '__main__':
    print_answer("challenge 1", challenge1)
    print_answer("challenge 2 (list approach)", challenge2_nlogn)
    print_answer("challenge 2 (heap approach)", challenge2_logn)
