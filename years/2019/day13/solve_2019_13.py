"""
Solution for day 13 of year 2019
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

def parse_line(line):
    line = line.strip()
    return line

def parse_lines(lines):
    return [x for x in lines]

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    output = []
    intcode(deepcopy(data), [], output)
    solution1 = len([output[x] for x in range(2, len(output), 3) if output[x] == 2])

    # Part 2
    solution2 = '???'
    data[0] = 2
    input = []
    output = []
    pointer, relative_base = intcode(data, input, output)
    blocks = [(output[x[0]-2],output[x[0]-1]) for x in enumerate(output) if (x[0]+1) % 3 == 0 and x[1] == 2]
    ball_x = output[[x for x in enumerate(output) if (x[0]+1) % 3 == 0 and x[1] == 4][0][0] -2]
    paddle_x = output[[x for x in enumerate(output) if (x[0]+1) % 3 == 0 and x[1] == 3][0][0] -2]
    while len(blocks) > 0:
        if ball_x > paddle_x:
            input.append(1)
        elif ball_x < paddle_x:
            input.append(-1)
        else:
            input.append(0)
        output.clear()
        pointer, relative_base = intcode(data, input, output, pointer, relative_base)
        ball_check = [x for x in enumerate(output) if (x[0]+1) % 3 == 0 and x[1] == 4]
        if (len(ball_check)):
            ball_x = output[ball_check[0][0] -2]
        paddle_check = [x for x in enumerate(output) if (x[0]+1) % 3 == 0 and x[1] == 3]
        if (len(paddle_check)):
            paddle_x = output[paddle_check[0][0] -2]
        empty_coords = [(output[x[0]-2],output[x[0]-1]) for x in enumerate(output) if (x[0]+1) % 3 == 0 and x[1] == 0]
        for empty in empty_coords:
            if empty in blocks:
                blocks.remove(empty)

    solution2 = output[output.index(-1)+2]

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
