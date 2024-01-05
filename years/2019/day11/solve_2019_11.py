"""
Solution for day 11 of year 2019
"""

import os
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return [int(x) for x in inputdata.read().split(',')]

def intcode(data, input = [], output = [], pointer = 0, relative_base = 0):
    while data[pointer] != 99:
        opcode = data[pointer] % 100
        if opcode == 1:
            index = intcode_get_index(3,data,pointer,relative_base)
            data[index] = data[intcode_get_index(1,data,pointer,relative_base)] + data[intcode_get_index(2,data,pointer,relative_base)]
            pointer += 4
        elif opcode == 2:
            index = intcode_get_index(3,data,pointer,relative_base)
            data[index] = data[intcode_get_index(1,data,pointer,relative_base)] * data[intcode_get_index(2,data,pointer,relative_base)]
            pointer += 4
        elif opcode == 3:
            if len(input) == 0:
                return pointer, relative_base
            index = intcode_get_index(1,data,pointer,relative_base)
            data[index] = input.pop(0)
            pointer += 2
        elif opcode == 4:
            output.append(data[intcode_get_index(1,data,pointer,relative_base)])
            pointer += 2
        elif opcode == 5:
            if data[intcode_get_index(1,data,pointer,relative_base)] != 0:
                pointer = data[intcode_get_index(2,data,pointer,relative_base)]
            else:
                pointer += 3
        elif opcode == 6:
            if data[intcode_get_index(1,data,pointer,relative_base)] == 0:
                pointer = data[intcode_get_index(2,data,pointer,relative_base)]
            else:
                pointer += 3
        elif opcode == 7:
            index = intcode_get_index(3,data,pointer,relative_base)
            if data[intcode_get_index(1,data,pointer,relative_base)] < data[intcode_get_index(2,data,pointer,relative_base)]:
                data[index] = 1
            else:
                data[index] = 0
            pointer += 4
        elif opcode == 8:
            index = intcode_get_index(3,data,pointer,relative_base)
            if data[intcode_get_index(1,data,pointer,relative_base)] == data[intcode_get_index(2,data,pointer,relative_base)]:
                data[index] = 1
            else:
                data[index] = 0
            pointer += 4
        elif opcode == 9:
            relative_base += data[intcode_get_index(1,data,pointer,relative_base)]
            pointer += 2
        else:
            print (data)
            print("ERR: UNKNOWN OPCODE: " + str(data[pointer]))
            exit()
    return pointer, relative_base

def intcode_get_index(no, data, pointer, relative_base):
    mode = 0
    if data[pointer] >= pow(10,1+no):
        tostr = str(data[pointer])
        mode = int(tostr[len(tostr)-2-no])
    index_to_return = pointer + no
    if mode == 0:
        index_to_return = data[pointer+no]
    elif mode == 2:
        index_to_return = relative_base + data[pointer+no]
    intcode_expand(data, index_to_return)
    return index_to_return

def intcode_expand(data, index):
    while index >= len(data):
        data.append(0)

def do_paint(data, first_input):
    data = deepcopy(data)
    pointer = 0
    input = [first_input]
    output = []
    relative_base = 0
    pos = (0,0)
    direction = (0,-1)
    to_paint = {}
    while data[pointer] != 99:
        pointer, relative_base = intcode(data, input, output, pointer, relative_base)
        to_paint[pos] = output[-2]
        if output[-1] == 0:
            direction = (direction[1], -direction[0])
        else:
            direction = (-direction[1], direction[0])
        pos = (pos[0] + direction[0], pos[1] + direction[1])
        if pos in to_paint:
            input.append(to_paint[pos])
        else:
            input.append(0)
    return to_paint

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    result = do_paint(data, 0)
    solution1 = len(result)

    # Part 2
    result = do_paint(data, 1)
    keys = [x for x in result]
    min_x = min([x[0] for x in keys])
    max_x = max([x[0] for x in keys])
    min_y = min([x[1] for x in keys])
    max_y = max([x[1] for x in keys])
    output = ''
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x,y) in result and result[(x,y)] == 1:
                output += '█'
            else:
                output += ' '
        output += '\n'

    solution2 = output
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
