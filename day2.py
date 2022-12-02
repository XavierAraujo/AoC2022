from enum import Enum
from utils import print_answer

CHALLENGE_INPUT = "./resources/day2-input1.txt"


class SHAPE(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class RESULT(Enum):
    LOSS = 0
    DRAW = 3
    VICTORY = 6


INPUT_TO_SHAPE = {'A': SHAPE.ROCK, 'B': SHAPE.PAPER, 'C': SHAPE.SCISSORS,
                  'X': SHAPE.ROCK, 'Y': SHAPE.PAPER, 'Z': SHAPE.SCISSORS}
INPUT_TO_RESULT = {'X': RESULT.LOSS, 'Y': RESULT.DRAW, 'Z': RESULT.VICTORY}


def challenge1():
    total_score = 0
    with open(CHALLENGE_INPUT, 'r') as f:
        for line in f.read().splitlines():
            opponent_move, own_move = get_shapes_from_input(line)
            total_score += calculate_round_score(opponent_move, own_move)
    return total_score


def challenge2():
    total_score = 0
    with open(CHALLENGE_INPUT, 'r') as f:
        for line in f.read().splitlines():
            opponent_move, result = get_shapes_and_result_from_input(line)
            own_move = get_own_shape_from_result(opponent_move, result)
            total_score += calculate_round_score(opponent_move, own_move)
    return total_score


def get_shapes_from_input(input):
    opponent_input, own_input = tuple(input.split(' '))
    return INPUT_TO_SHAPE[opponent_input], INPUT_TO_SHAPE[own_input]


def calculate_round_score(opponent_shape, own_shape):
    result = calculate_result(opponent_shape, own_shape)
    return result.value + own_shape.value


def calculate_result(opponent_shape, own_shape):
    if opponent_shape == own_shape:
        return RESULT.DRAW
    elif (own_shape == SHAPE.ROCK and opponent_shape == SHAPE.PAPER) \
            or (own_shape == SHAPE.PAPER and opponent_shape == SHAPE.SCISSORS) \
            or (own_shape == SHAPE.SCISSORS and opponent_shape == SHAPE.ROCK):
        return RESULT.LOSS
    else:
        return RESULT.VICTORY


def get_shapes_and_result_from_input(input):
    opponent_input, result_input = tuple(input.split(' '))
    return INPUT_TO_SHAPE[opponent_input], INPUT_TO_RESULT[result_input]


def get_own_shape_from_result(opponent_shape, result):
    if result == RESULT.DRAW:
        return opponent_shape
    elif (result == RESULT.VICTORY and opponent_shape == SHAPE.PAPER) \
            or (result == RESULT.LOSS and opponent_shape == SHAPE.ROCK):
        return SHAPE.SCISSORS
    elif (result == RESULT.VICTORY and opponent_shape == SHAPE.SCISSORS) \
            or (result == RESULT.LOSS and opponent_shape == SHAPE.PAPER):
        return SHAPE.ROCK
    else:
        return SHAPE.PAPER


if __name__ == '__main__':
    print_answer("challenge 1", challenge1)
    print_answer("challenge 2", challenge2)
