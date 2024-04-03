"""
Solution for day 18 of year 2021
"""

import os
import json
from copy import deepcopy
from math import floor, ceil

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return json.loads(line.strip())

def add(num1, num2):
    num = [num1, num2]
    fix = True
    while fix:
        fix = False
        data = { 'lastnum': [], 'explodevalue': None, 'explodevalue_new': False, 'leftnumpos': None, 'nextnumset': False }
        explode_lvl(num, 4, 0, data, [])
        fix = data['explodevalue'] != None
        if not fix:
            data = { 'didsplit': False }
            split(num, data)
            fix = data['didsplit'] == True
    return num

def split(num, data):
    if isinstance(num[0], list) and not data['didsplit']:
        split(num[0], data)
    elif isinstance(num[0], int) and num[0] > 9 and not data['didsplit']:
        num[0] = [floor(num[0]/2),ceil(num[0]/2)]
        data['didsplit'] = True
    if isinstance(num[1], list) and not data['didsplit']:
        split(num[1], data)
    elif isinstance(num[1], int) and num[1] > 9 and not data['didsplit']:
        num[1] = [floor(num[1]/2),ceil(num[1]/2)]
        data['didsplit'] = True


def explode_lvl(num, explode_at, current_lvl, data, pos):
    if isinstance(num, list) and explode_at == current_lvl and data['explodevalue'] == None:
        data['explodevalue'] = num
        data['explodevalue_new'] = True
        return
    localpos = deepcopy(pos)
    localpos.append(0)
    if isinstance(num[0], list):
        explode_lvl(num[0], explode_at, current_lvl + 1, data, localpos)
        if data['explodevalue_new']:
            data['explodevalue_new'] = False
            num[0] = 0
            data['leftnumpos'] = deepcopy(data['lastnum'])
    else:
        if data['explodevalue'] != None and not data['nextnumset']:
            num[0] += data['explodevalue'][1]
            data['nextnumset'] = True
        data['lastnum'] = localpos
    localpos = deepcopy(pos)
    localpos.append(1)
    if isinstance(num[1], list):
        explode_lvl(num[1], explode_at, current_lvl + 1, data, localpos)
        if data['explodevalue_new']:
            data['explodevalue_new'] = False
            num[1] = 0
            data['leftnumpos'] = deepcopy(data['lastnum'])
    else:
        if data['explodevalue'] != None and not data['nextnumset']:
            num[1] += data['explodevalue'][1]
            data['nextnumset'] = True
        data['lastnum'] = localpos
    if current_lvl == 0 and data['leftnumpos'] != None and data['leftnumpos'] != []:
        add_data_at_pos(num, data['explodevalue'][0], data['leftnumpos'])
    return

def add_data_at_pos(num, data, pos):
    if len(pos) == 1:
        num[pos[0]] += data
    else:
        add_data_at_pos(num[pos.pop(0)], data, pos)

def list_sum(data):
    copydata = deepcopy(list(data))
    result = copydata.pop(0)
    while len(copydata) > 0:
        result = add(result, copydata.pop(0))
    return result

def magnitude(data):
    if isinstance(data, int):
        return data
    return magnitude(data[0]) * 3 + magnitude(data[1]) * 2

def find_largest_sum_magnitude(data):
    biggest = 0
    number = len(data)
    for x in range(number - 1):
        for y in range(x+1, number):
            x1 = deepcopy(data[x])
            x2 = deepcopy(data[x])
            y1 = deepcopy(data[y])
            y2 = deepcopy(data[y])
            mag = magnitude(add(x1, y1))
            if mag > biggest:
                biggest = mag
            mag = magnitude(add(y2, x2))
            if mag > biggest:
                biggest = mag

    return biggest

def solve(data):
    """Solve the puzzle for the given input"""
    data2 = deepcopy(data)
    # Part 1
    solution1 = magnitude(list_sum(data))

    # Part 2
    solution2 = find_largest_sum_magnitude(data2)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
