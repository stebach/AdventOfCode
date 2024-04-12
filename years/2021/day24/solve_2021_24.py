"""
Solution for day 24 of year 2021
"""

import os
from math import floor
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip().split(' ')
    result = [line.pop(0)]
    while len(line):
        next_attr = line.pop(0)
        if next_attr in ('w','x','y','z'):
            result.append(next_attr)
        else:
            result.append(int(next_attr))
    return tuple(result)

def run(data, vars):
    idx = 0
    names = ('w','x','y','z')
    state = [0,0,0,0]
    orig_len = len(vars)
    local_vars = deepcopy(vars)
    while idx < len(data):
        cmd = data[idx]
        if (cmd[0] == 'inp'):
            state[names.index(cmd[1])] = local_vars.pop(0)
        elif (cmd[0] == 'add'):
            if cmd[2] in names:
                state[names.index(cmd[1])] += state[names.index(cmd[2])]
            else:
                state[names.index(cmd[1])] += cmd[2]
        elif (cmd[0] == 'mod'):
            if cmd[2] in names:
                state[names.index(cmd[1])] = state[names.index(cmd[1])] % state[names.index(cmd[2])]
            else:
                state[names.index(cmd[1])] = state[names.index(cmd[1])] % cmd[2]
        elif (cmd[0] == 'div'):
            if cmd[2] in names:
                state[names.index(cmd[1])] = int(floor(state[names.index(cmd[1])] / state[names.index(cmd[2])]))
            else:
                state[names.index(cmd[1])] = int(floor(state[names.index(cmd[1])] / cmd[2]))
        elif (cmd[0] == 'mul'):
            if cmd[2] in names:
                state[names.index(cmd[1])] *= state[names.index(cmd[2])]
            else:
                state[names.index(cmd[1])] *= cmd[2]
        elif (cmd[0] == 'eql'):
            if cmd[2] in names:
                state[names.index(cmd[1])] = 1 if state[names.index(cmd[1])] == state[names.index(cmd[2])] else 0
            else:
                state[names.index(cmd[1])] = 1 if state[names.index(cmd[1])] == cmd[2] else 0
        else:
            print("UNKNOWN CMD: " + cmd[0])
            exit()
        idx += 1
    return state

def find_highest(data):


    found = False
    print("XXX")
    print (run(data, [5,1,9,8,3,9,9,9,9,4,7,9,9,9]))
    exit()
    input = [5,1,9,8,3,9,9,9,9,4,7,9,9,9]
    while not found:
        check = run(data, input, True)
        if isinstance(check, int):
            input[check] -= 1
            for pos in range(check + 1, 14):
                input[pos] = 9
        else:
            found = True
        print(input)
    print(input)
    print (run(data, [1,1,1,1,1,1,1,1,1,1,1,1,1,1], True))
    print (run(data, [5,1,9,8,3,9,9,9,9,4,7,9,9,9]))

def solve(data):
    """Solve the puzzle for the given input"""
    # index            0   1   2    3   4   5   6   7   8   9  10  11  12  13
    # group            0   1   2    2   3   3   1   4   4   5   6   6   5   0
    div  = [ 1,  1,  1,  26,  1, 26, 26,  1, 26,  1,  1, 26, 26, 26 ]
    add  = [11, 11, 15, -14, 10,  0, -6, 13, -3, 13, 15, -2, -9, -2 ]
    add2 = [ 6, 14, 13,   1,  6, 13,  6,  3,  8, 14,  4,  7, 15,  1 ]
    # 0 -> 13:  +6 +  -2 -> +4
    # 1 -> 6:  +14 +  -6 -> +8
    # 2 -> 3 : +13 + -14 -> -1
    # 4 -> 5:   +6 +   0 -> +6
    # 7 -> 8:   +3 +  -3 -> +0
    # 9 -> 12: +14 +  -9 -> +5
    # 10 -> 11: +4 +  -2 -> +2

    results = []
    for group0 in range(1, 6):
        group1 = 1
        for group2 in range(2, 10):
            for group3 in range(1, 4):
                for group4 in range(1, 10):
                    for group5 in range(1, 5):
                        for group6 in range(1, 8):
                            toCheck = [group0, group1, group2, group2 - 1, group3, group3 + 6, group1 + 8, group4, group4, group5, group6, group6 + 2, group5 + 5, group0 + 4]
                            check = run(data, toCheck)
                            if check[3] == 0:
                                results.append(sum([pow(10,13-x[0]) * x[1] for x in enumerate(toCheck)]))


    results.sort()
    # Part 1
    solution1 = results[-1]

    # Part 2
    solution2 = results[0]

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

