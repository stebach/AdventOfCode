"""
Solution for day 11 of year 2016
"""

import os
from copy import deepcopy
from queue import PriorityQueue
import time

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = {
        'elevator': 0,
        'floors': []
    }
    for line in lines:
        line = line.strip()[4:-1].split(' floor contains')
        floor = -1
        if line[0] == 'first':
            floor = 0
        elif line[0] == 'second':
            floor = 1
        elif line[0] == 'third':
            floor = 2
        elif line[0] == 'fourth':
            floor = 3
        else:
            print("UNKNOWN FLOOR: " + line[0])
            exit()
        if line[1][0:3] == ' a ':
            line[1] = line[1][3:]
        while len(result['floors']) <= floor:
            result['floors'].append([])
        parts = line[1].replace(', a ',' and a ').replace(', and a ',' and a ').split(' and a ')
        for part in parts:
            if part == ' nothing relevant':
                continue
            part = part.split(' ')
            if part[1] == 'microchip':
                result['floors'][floor].append([part[0][:-11], part[1]])
            elif part[1] == 'generator':
                result['floors'][floor].append([part[0],part[1]])
            else:
                print("UNKNOWN PART: " + part[1])
                exit()
    return result

def move_to_top_floor(data):
    queue = PriorityQueue()
    queue.put((0, 0, deepcopy(data)))
    index = 1
    seen = set()

    while queue.qsize() > 0:
        check = queue.get()
        check[2]['floors'] = [[y for y in sorted(x)] for x in check[2]['floors']]
        if sum ([len(x) for x in check[2]['floors'][0:-1]]) == 0:
            return check[0]
        for item1 in range(len(check[2]['floors'][check[2]['elevator']])):
            add_if_valid(queue, check, check[2]['elevator'] - 1, [check[2]['floors'][check[2]['elevator']][item1]], index, seen)
            index += 1
            add_if_valid(queue, check, check[2]['elevator'] + 1, [check[2]['floors'][check[2]['elevator']][item1]], index, seen)
            index += 1
            for item2 in range(item1 + 1, len(check[2]['floors'][check[2]['elevator']])):
                add_if_valid(queue, check, check[2]['elevator'] -1, [check[2]['floors'][check[2]['elevator']][item1], check[2]['floors'][check[2]['elevator']][item2]], index, seen)
                index += 1
                add_if_valid(queue, check, check[2]['elevator'] + 1, [check[2]['floors'][check[2]['elevator']][item1], check[2]['floors'][check[2]['elevator']][item2]], index, seen)
                index += 1

def add_if_valid(queue, check, floor_to, items_to_move, index, seen):
    if floor_to < 0 or floor_to >= len(check[2]['floors']):
        return
    check = deepcopy(check)
    for x in items_to_move:
        check[2]['floors'][check[2]['elevator']].remove(x)
    for x in items_to_move:
        check[2]['floors'][floor_to].append(x)
    check[2]['floors'][floor_to] = sorted(check[2]['floors'][floor_to])
    check[2]['elevator'] = floor_to
    if validate_floors(check[2]['floors']) and not make_hashable(check[2]) in seen:
        seen.add(make_hashable(check[2]))
        queue.put((check[0] + 1, index, check[2]))

def make_hashable(data):
    return (data['elevator'], tuple([(sum([y[1] == 'microchip' for y in x]), sum([y[1] == 'generator' for y in x])) for x in data['floors']]))

def validate_floors(floors):
    for floor in floors:
        has_generators = len([x for x in floor if x[1] == 'generator']) > 0
        has_unprotected_microchips = len([x for x in floor if x[1] == 'microchip' and [x[0], 'generator'] not in floor]) > 0
        if has_generators and has_unprotected_microchips:
            return False
    return True

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = move_to_top_floor(data)

    # Part 2
    data['floors'][0].append(['elerium', 'generator'])
    data['floors'][0].append(['elerium', 'microchip'])
    data['floors'][0].append(['dilithium', 'generator'])
    data['floors'][0].append(['dilithium', 'microchip'])
    solution2 = move_to_top_floor(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
