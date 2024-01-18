"""
Solution for day 21 of year 2019
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

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    output = []
    input = []
    input += [ord(x) for x in [*"NOT A J\n"]]
    input += [ord(x) for x in [*"NOT B T\n"]]
    input += [ord(x) for x in [*"OR T J\n"]]
    input += [ord(x) for x in [*"NOT C T\n"]]
    input += [ord(x) for x in [*"OR T J\n"]]
    input += [ord(x) for x in [*"AND D J\n"]]
    input += [ord(x) for x in [*"WALK\n"]]

    intcode(deepcopy(data),input,output)

    solution1 = output[-1]
    # Part 2
    output = []
    input = []
    input += [ord(x) for x in [*"NOT A J\n"]]
    input += [ord(x) for x in [*"NOT B T\n"]]
    input += [ord(x) for x in [*"OR T J\n"]]
    input += [ord(x) for x in [*"NOT C T\n"]]
    input += [ord(x) for x in [*"OR T J\n"]]
    input += [ord(x) for x in [*"AND D J\n"]]
    input += [ord(x) for x in [*"NOT J T\n"]]
    input += [ord(x) for x in [*"OR H T\n"]]
    input += [ord(x) for x in [*"OR E T\n"]]
    input += [ord(x) for x in [*"AND T J\n"]]
    input += [ord(x) for x in [*"RUN\n"]]

    intcode(deepcopy(data),input,output)

    solution2 = output[-1]

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
