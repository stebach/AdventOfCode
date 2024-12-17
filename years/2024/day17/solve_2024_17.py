"""
Solution for day 17 of year 2024
"""

import os
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = {
        'registers': {},
        'program': None
    }

    for line in lines:
        if line.startswith('Register '):
            register, value = line.split(': ')
            result['registers'][register.split(' ')[1]] = int(value)
        elif line.startswith('Program: '):
            result['program'] = list(map(int, line[9:].split(',')))

    return result

def get_output(data):
    localdata = deepcopy(data)
    instruction_pointer = 0
    output = []

    while instruction_pointer < len(localdata['program']):
        if localdata['program'][instruction_pointer] == 0: #adv
            localdata['registers']['A'] = localdata['registers']['A'] // pow(2, get_combo(localdata['program'][instruction_pointer + 1], localdata['registers']))
        elif localdata['program'][instruction_pointer] == 1: #bxl
            localdata['registers']['B'] = localdata['registers']['B'] ^ localdata['program'][instruction_pointer + 1]
        elif localdata['program'][instruction_pointer] == 2: #bst
            localdata['registers']['B'] = get_combo(localdata['program'][instruction_pointer + 1], localdata['registers']) % 8
        elif localdata['program'][instruction_pointer] == 3: #jnz
            if localdata['registers']['A'] != 0:
                instruction_pointer = localdata['program'][instruction_pointer + 1]
                continue
        elif localdata['program'][instruction_pointer] == 4: #bxc
            localdata['registers']['B'] = localdata['registers']['B'] ^ localdata['registers']['C']
        elif localdata['program'][instruction_pointer] == 5: #out
            output.append(get_combo(localdata['program'][instruction_pointer + 1], localdata['registers']) % 8)
        elif localdata['program'][instruction_pointer] == 6: #bdv
            localdata['registers']['B'] = localdata['registers']['A'] // pow(2, get_combo(localdata['program'][instruction_pointer + 1], localdata['registers']))
        elif localdata['program'][instruction_pointer] == 7: #cdv
            localdata['registers']['C'] = localdata['registers']['A'] // pow(2, get_combo(localdata['program'][instruction_pointer + 1], localdata['registers']))

        instruction_pointer += 2

    return output

def get_combo(instruction, registers):
    if instruction < 4:
        return instruction
    return registers[chr(61 + instruction)]

def find_copy(data):
    # only works as the input will do a A = A // 8 before the jnz opcode 

    queue = [[]]
    results = []

    while len(queue) > 0:
        possibility = queue.pop(0)
        for j in range(8):
            new_a = 0
            check = possibility + [j]
            for pos,val in enumerate(check):
                new_a += val * pow(8, len(check) - 1 - pos)

            data['registers']['A'] = new_a

            output = get_output(data)

            if output == data['program'][len(data['program']) - len(output):]:
                if len(output) == len(data['program']):
                    results.append(new_a)
                else:
                    queue.append(check)

    return min(results)

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = ",".join([str(x) for x in get_output(data)])

    # Part 2
    solution2 = find_copy(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

