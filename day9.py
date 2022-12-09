from utils import print_answer
import re
from dataclasses import dataclass
from enum import Enum

CHALLENGE_INPUT = "./resources/day9-input1.txt"


class Direction(Enum):
    NONE = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    UP_RIGHT = 5
    DOWN_RIGHT = 6
    UP_LEFT = 7
    DOWN_LEFT = 8


@dataclass(unsafe_hash=True)
class Position:
    x: int
    y: int


@dataclass
class Move:
    direction: Direction
    steps: int


def challenge1():
    with open(CHALLENGE_INPUT, 'r') as f:
        tail_positions = get_positions_visited_by_tail(f.read().splitlines(), 2)
        return len(tail_positions)


def challenge2():
    with open(CHALLENGE_INPUT, 'r') as f:
        tail_positions = get_positions_visited_by_tail(f.read().splitlines(), 10)
        return len(tail_positions)


def get_positions_visited_by_tail(head_movements_input, knot_number):
    knots = [Position(0, 0)] * knot_number
    tail_positions = set()
    for head_movement_input in head_movements_input:
        head_move = parse_move(head_movement_input)
        for i in range(head_move.steps):
            knot_move_direction = head_move.direction
            knots[0] = get_position_after_move(knots[0], knot_move_direction)  # move head
            for j in range(len(knots) - 1):  # evaluate which knots should be dragged due to the movement of the head
                knot_move_direction = get_follower_move_direction(knots[j + 1], knots[j])
                knots[j + 1] = get_position_after_move(knots[j + 1], knot_move_direction)
                if knot_move_direction == Direction.NONE:  # optimization
                    break  # if a given knot does not move we don't need to check the next ones
            tail_positions.add(knots[-1])
    return tail_positions


def parse_move(line):
    res = re.match(r"([UDLR]) ([0-9]*)", line)
    letter = res.group(1)
    steps = int(res.group(2))
    letter2direction = {
        "U": Direction.UP,
        "D": Direction.DOWN,
        "R": Direction.RIGHT,
        "L": Direction.LEFT
    }
    return Move(letter2direction.get(letter), steps)


def get_follower_move_direction(follower_position: Position, leader_position: Position):
    if should_follower_move(follower_position, leader_position) and follower_position.y == leader_position.y:  # Move horizontally
        return Direction.RIGHT if leader_position.x > follower_position.x else Direction.LEFT
    if should_follower_move(follower_position, leader_position) and follower_position.x == leader_position.x:  # Move vertically
        return Direction.UP if leader_position.y > follower_position.y else Direction.DOWN
    if should_follower_move(follower_position, leader_position):
        if leader_position.x < follower_position.x and leader_position.y > follower_position.y:
            return Direction.UP_LEFT
        elif leader_position.x < follower_position.x and leader_position.y < follower_position.y:
            return Direction.DOWN_LEFT
        elif leader_position.x > follower_position.x and leader_position.y > follower_position.y:
            return Direction.UP_RIGHT
        elif leader_position.x > follower_position.x and leader_position.y < follower_position.y:
            return Direction.DOWN_RIGHT
    return Direction.NONE


def should_follower_move(follower_position, leader_position):
    return abs(follower_position.x - leader_position.x) > 1 or abs(follower_position.y - leader_position.y) > 1


def get_position_after_move(current_position, direction):
    if direction == Direction.NONE:
        return current_position
    if direction == Direction.UP:
        return Position(current_position.x, current_position.y + 1)
    if direction == Direction.DOWN:
        return Position(current_position.x, current_position.y - 1)
    if direction == Direction.LEFT:
        return Position(current_position.x - 1, current_position.y)
    if direction == Direction.RIGHT:
        return Position(current_position.x + 1, current_position.y)
    if direction == Direction.UP_RIGHT:
        return Position(current_position.x + 1, current_position.y + 1)
    if direction == Direction.DOWN_RIGHT:
        return Position(current_position.x + 1, current_position.y - 1)
    if direction == Direction.UP_LEFT:
        return Position(current_position.x - 1, current_position.y + 1)
    if direction == Direction.DOWN_LEFT:
        return Position(current_position.x - 1, current_position.y - 1)


if __name__ == '__main__':
    print_answer("challenge 1", challenge1)
    print_answer("challenge 2", challenge2)
