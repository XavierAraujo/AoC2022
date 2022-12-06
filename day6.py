from utils import print_answer

CHALLENGE_INPUT = "./resources/day6-input1.txt"
MARKER_SIZE_1 = 4
MARKER_SIZE_2 = 14


def challenge1():
    with open(CHALLENGE_INPUT, 'r') as f:
        return get_char_number_before_marker(f.read(), MARKER_SIZE_1)


def challenge2():
    with open(CHALLENGE_INPUT, 'r') as f:
        return get_char_number_before_marker(f.read(), MARKER_SIZE_2)


def get_char_number_before_marker(stream, marker_size):
    chars = {}
    [increment_char(chars, stream[i]) for i in range(0, marker_size)]
    for i in range(marker_size, len(stream)):
        if len(chars) == marker_size:
            return i

        decrement_char(chars, stream[i-marker_size])
        if chars[stream[i-marker_size]] == 0:
            del chars[stream[i-marker_size]]
        increment_char(chars, stream[i])


def decrement_char(chars, char):
    chars[char] = chars.get(char, 0) - 1


def increment_char(chars, char):
    chars[char] = chars.get(char, 0) + 1


if __name__ == '__main__':
    print_answer("challenge 1", challenge1)
    print_answer("challenge 2", challenge2)
