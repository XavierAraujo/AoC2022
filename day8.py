from utils import print_answer

CHALLENGE_INPUT = "./resources/day8-input1.txt"


def challenge1():
    count = 0
    with open(CHALLENGE_INPUT, 'r') as f:
        matrix = parse_input_to_matrix(f.read().splitlines())
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if is_tree_visible(matrix, x, y):
                    count += 1
    return count


def challenge2():
    max_scenic_score = -1
    with open(CHALLENGE_INPUT, 'r') as f:
        matrix = parse_input_to_matrix(f.read().splitlines())
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                scenic_score = calculate_tree_scenic_score(matrix, x, y)
                if scenic_score > max_scenic_score:
                    max_scenic_score = scenic_score
    return max_scenic_score


def parse_input_to_matrix(lines):
    matrix = []
    for line in lines:
        matrix.append([int(tree_size) for tree_size in line])
    return matrix


def is_tree_visible(matrix, tree_x, tree_y):
    return is_tree_left_visible(matrix, tree_x, tree_y) or \
           is_tree_right_visible(matrix, tree_x, tree_y) or \
           is_tree_up_visible(matrix, tree_x, tree_y) or \
           is_tree_down_visible(matrix, tree_x, tree_y)


def is_tree_left_visible(matrix, tree_x, tree_y):
    for x in range(tree_x):
        if matrix_tree_size(matrix, x, tree_y) >= matrix_tree_size(matrix, tree_x, tree_y):
            return False
    return True


def is_tree_right_visible(matrix, tree_x, tree_y):
    for x in range(tree_x+1, len(matrix[tree_x])):
        if matrix_tree_size(matrix, x, tree_y) >= matrix_tree_size(matrix, tree_x, tree_y):
            return False
    return True


def is_tree_up_visible(matrix, tree_x, tree_y):
    for y in range(tree_y):
        if matrix_tree_size(matrix, tree_x, y) >= matrix_tree_size(matrix, tree_x, tree_y):
            return False
    return True


def is_tree_down_visible(matrix, tree_x, tree_y):
    for y in range(tree_y+1, len(matrix)):
        if matrix_tree_size(matrix, tree_x, y) >= matrix_tree_size(matrix, tree_x, tree_y):
            return False
    return True


def calculate_tree_scenic_score(matrix, tree_x, tree_y):
    return calculate_tree_left_scenic_score(matrix, tree_x, tree_y) * \
           calculate_tree_right_scenic_score(matrix, tree_x, tree_y) * \
           calculate_tree_up_scenic_score(matrix, tree_x, tree_y) * \
           calculate_tree_down_scenic_score(matrix, tree_x, tree_y)


def calculate_tree_left_scenic_score(matrix, tree_x, tree_y):
    count = 0
    for x in reversed(range(tree_x)):
        count += 1
        if matrix_tree_size(matrix, x, tree_y) >= matrix_tree_size(matrix, tree_x, tree_y):
            break
    return count


def calculate_tree_right_scenic_score(matrix, tree_x, tree_y):
    count = 0
    for x in range(tree_x+1, len(matrix[tree_x])):
        count += 1
        if matrix_tree_size(matrix, x, tree_y) >= matrix_tree_size(matrix, tree_x, tree_y):
            break
    return count


def calculate_tree_up_scenic_score(matrix, tree_x, tree_y):
    count = 0
    for y in reversed(range(tree_y)):
        count += 1
        if matrix_tree_size(matrix, tree_x, y) >= matrix_tree_size(matrix, tree_x, tree_y):
            break
    return count


def calculate_tree_down_scenic_score(matrix, tree_x, tree_y):
    count = 0
    for y in range(tree_y+1, len(matrix)):
        count += 1
        if matrix_tree_size(matrix, tree_x, y) >= matrix_tree_size(matrix, tree_x, tree_y):
            break
    return count


def matrix_tree_size(matrix, x, y):
    return matrix[y][x]


if __name__ == '__main__':
    print_answer("challenge 1", challenge1)
    print_answer("challenge 2", challenge2)
