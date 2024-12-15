"""
Solution for day 15 of year 2024
"""

import os
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    coords = []
    robot = None
    moves = []
    walls = []
    moves_dict = {
        '>': 0,
        'v': 1,
        '<': 2,
        '^': 3,
    }
    height = 0
    parse_moves = False
    for y, row in enumerate(lines):
        if parse_moves:
            for move in row.strip():
                moves.append(moves_dict[move])
            continue
        if len(row.strip()) == 0:
            parse_moves = True
            height = y - 2
            continue
        for x, cell in enumerate(row):
            if cell == 'O':
                coords.append((x - 1, y - 1))
            elif cell == '@':
                robot = (x - 1, y - 1)
            elif cell == '#':
                walls.append((x - 1, y - 1))
                pass

    return {
        'w': len(lines[0].strip()) - 2,
        'h': height,
        'coords': tuple(coords),
        'robot': robot,
        'moves': tuple(moves),
        'walls': tuple(walls),
    }


def get_gps_sum(data):
    robot = data['robot']
    coords = list(data['coords'])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    walls = data['walls']
    w = data['w']
    h = data['h']

    for move in data['moves']:
        if can_move(robot, directions[move], coords, w, h, walls):
            robot = do_move(robot, directions[move], coords)

    return sum([x[0] + 100*x[1] + 101 for x in coords])

def get_gps_sum_double(data):
    robot = (data['robot'][0] * 2, data['robot'][1])
    coords_l = [(x * 2, y) for x, y in data['coords']]
    coords_r = [(x * 2 + 1, y) for x, y in data['coords']]
    walls = tuple([(x * 2, y) for x, y in data['walls']] + [(x * 2 + 1, y) for x, y in data['walls']])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    w = data['w'] * 2
    h = data['h']

    for move in data['moves']:
        if can_move_double(robot, directions[move], coords_l, coords_r, w, h, walls):
            robot = do_move_double(robot, directions[move], coords_l, coords_r)

    for y in range(h):
        for x in range(w):
            if (x, y) == robot:
                print('@', end='')
            elif (x, y) in coords_l:
                print('[', end='')
            elif (x, y) in coords_r:
                print(']', end='')
            elif (x, y) in walls:
                print('#', end='')
            else:
                print('.', end='')
        print("")

    return sum([x[0] + 100*x[1] + 102 for x in coords_l])

def can_move(object, direction, coords, w, h, walls):
    target = (object[0] + direction[0], object[1] + direction[1])
    if target[0] < 0 or target[0] >= w or target[1] < 0 or target[1] >= h or target in walls:
        return False
    if target in coords:
        return can_move(target, direction, coords, w, h, walls)
    return True

def do_move(object, direction, coords, is_robot=True):
    target = (object[0] + direction[0], object[1] + direction[1])
    if target in coords:
        do_move(target, direction, coords, False)
    if not is_robot:
        coords.remove(object)
        coords.append(target)
    if is_robot:
        return target

def can_move_double(object, direction, coords_l, coords_r, w, h, walls):
    target = (object[0] + direction[0], object[1] + direction[1])
    if target[0] < 0 or target[0] >= w or target[1] < 0 or target[1] >= h or target in walls:
        return False
    if direction[1] != 0:
        if target in coords_l:
            return can_move_double(target, direction, coords_l, coords_r, w, h, walls) \
                and can_move_double((target[0] + 1, target[1]), direction, coords_l, coords_r, w, h, walls)
        if target in coords_r:
            return can_move_double(target, direction, coords_l, coords_r, w, h, walls) \
                and can_move_double((target[0] - 1, target[1]), direction, coords_l, coords_r, w, h, walls)
    elif target in coords_l or target in coords_r:
        return can_move_double(target, direction, coords_l, coords_r, w, h, walls)
    return True

def do_move_double(object, direction, coords_l, coords_r, is_robot=True):
    target = (object[0] + direction[0], object[1] + direction[1])
    if direction[1] != 0:
        if target in coords_l:
            do_move_double(target, direction, coords_l, coords_r, False)
            do_move_double((target[0] + 1, target[1]), direction, coords_l, coords_r, False)
        if target in coords_r:
            do_move_double(target, direction, coords_l, coords_r, False)
            do_move_double((target[0] - 1, target[1]), direction, coords_l, coords_r, False)
    elif target in coords_l or target in coords_r:
        do_move_double(target, direction, coords_l, coords_r, False)
    if not is_robot:
        if object in coords_l:
            coords_l.remove(object)
            coords_l.append(target)
        else:
            coords_r.remove(object)
            coords_r.append(target)
    if is_robot:
        return target

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_gps_sum(data)

    # Part 2
    solution2 = get_gps_sum_double(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

