"""
Solution for day 16 of year 2018
"""

import os
from copy import deepcopy

OPCODE_ADDR=0
OPCODE_ADDI=1
OPCODE_MULR=2
OPCODE_MULI=3
OPCODE_BANR=4
OPCODE_BANI=5
OPCODE_BORR=6
OPCODE_BORI=7
OPCODE_SETR=8
OPCODE_SETI=9
OPCODE_GTIR=10
OPCODE_GTRI=11
OPCODE_GTRR=12
OPCODE_EQIR=13
OPCODE_EQRI=14
OPCODE_EQRR=15

registers = [0,0,0,0]

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    pos = 0
    samples = []
    instructions = []
    while pos < len(lines):
        if lines[pos][:8] == 'Before: ':
            samples.append(
                (
                    tuple([int(x) for x in lines[pos].strip()[9:-1].split(', ')]),
                    tuple([int(x) for x in lines[pos+1].strip().split(' ')]),
                    tuple([int(x) for x in lines[pos+2].strip()[9:-1].split(', ')])
                )
            )
            pos += 3
        elif len(lines[pos].strip()) > 0:
            instructions.append(tuple([int(x) for x in lines[pos].split(' ')]))

        pos += 1
    return (
        tuple(samples),
        tuple(instructions)
    )

def possible_opcodes(opcode):
    count = 0
    for x in range(16):
        for i in range(4):
            registers[i] = opcode[0][i]
        run_opcode((x, opcode[1][1], opcode[1][2], opcode[1][3]))
        if registers == list(opcode[2]):
            count += 1
    return count

def run_opcode(opcode_data):
    opcode, a, b, c = opcode_data
    if opcode == OPCODE_ADDR:
        registers[c] = registers[a] + registers[b]
    elif opcode == OPCODE_ADDI:
        registers[c] = registers[a] + b
    elif opcode == OPCODE_MULR:
        registers[c] = registers[a] * registers[b]
    elif opcode == OPCODE_MULI:
        registers[c] = registers[a] * b
    elif opcode == OPCODE_BANR:
        registers[c] = registers[a] & registers[b]
    elif opcode == OPCODE_BANI:
        registers[c] = registers[a] & b
    elif opcode == OPCODE_BORR:
        registers[c] = registers[a] | registers[b]
    elif opcode == OPCODE_BORI:
        registers[c] = registers[a] | b
    elif opcode == OPCODE_SETR:
        registers[c] = registers[a]
    elif opcode == OPCODE_SETI:
        registers[c] = a
    elif opcode == OPCODE_GTIR:
        registers[c] = 1 if a > registers[b] else 0
    elif opcode == OPCODE_GTRI:
        registers[c] = 1 if registers[a] > b else 0
    elif opcode == OPCODE_GTRR:
        registers[c] = 1 if registers[a] > registers[b] else 0
    elif opcode == OPCODE_EQIR:
        registers[c] = 1 if a == registers[b] else 0
    elif opcode == OPCODE_EQRI:
        registers[c] = 1 if registers[a] == b else 0
    elif opcode == OPCODE_EQRR:
        registers[c] = 1 if registers[a] == registers[b] else 0


def part1(data):
    """Solve part 1"""
    return len([y for y in [possible_opcodes(x) for x in data[0]] if y > 2])

def part2(data):
    """Solve part 2"""
    possibilities = [
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
    ]
    for opcode in data[0]:
        for o in range(16):
            if o in possibilities[opcode[1][0]]:
                for i in range(4):
                    registers[i] = opcode[0][i]
                run_opcode((o, opcode[1][1], opcode[1][2], opcode[1][3]))

                if registers != list(opcode[2]):
                    possibilities[opcode[1][0]].remove(o)

    found = []
    while sum([len(x) for x in possibilities]) > 16:
        check = [x[0] for x in possibilities if len(x) == 1 and x[0] not in found]
        for x in check:
            for i in range(16):
                if x in possibilities[i] and len(possibilities[i]) > 1:
                    possibilities[i].remove(x)
            found.append(x)
    match = [x[0] for x in possibilities]

    for i in range(4):
        registers[i] = 0
    
    for opcode in data[1]:
        run_opcode((match[opcode[0]], opcode[1], opcode[2], opcode[3]))
    
    return registers[0]

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
