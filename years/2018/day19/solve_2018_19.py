"""
Solution for day 19 of year 2018
"""

import os
from collections import deque
from itertools import islice
from math import ceil

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
OPCODE_IP=16

registers = [0,0,0,0,0,0]
instruction_register = 0
in_loop = False

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    parts = line.strip().split(' ')
    if parts[0] == '#ip':
        return (OPCODE_IP, int(parts[1]), 0, 0)
    elif parts[0] == 'addr':
        return (OPCODE_ADDR, int(parts[1]), int(parts[2]), int(parts[3]))
    elif parts[0] == 'addi':
        return (OPCODE_ADDI, int(parts[1]), int(parts[2]), int(parts[3]))
    elif parts[0] == 'mulr':
        return (OPCODE_MULR, int(parts[1]), int(parts[2]), int(parts[3]))
    elif parts[0] == 'muli':
        return (OPCODE_MULI, int(parts[1]), int(parts[2]), int(parts[3]))
    elif parts[0] == 'banr':
        return (OPCODE_BANR, int(parts[1]), int(parts[2]), int(parts[3]))
    elif parts[0] == 'bani':
        return (OPCODE_BANI, int(parts[1]), int(parts[2]), int(parts[3]))
    elif parts[0] == 'borr':
        return (OPCODE_BORR, int(parts[1]), int(parts[2]), int(parts[3]))
    elif parts[0] == 'bori':
        return (OPCODE_BORI, int(parts[1]), int(parts[2]), int(parts[3]))
    elif parts[0] == 'setr':
        return (OPCODE_SETR, int(parts[1]), int(parts[2]), int(parts[3]))
    elif parts[0] == 'seti':
        return (OPCODE_SETI, int(parts[1]), int(parts[2]), int(parts[3]))
    elif parts[0] == 'gtir':
        return (OPCODE_GTIR, int(parts[1]), int(parts[2]), int(parts[3]))
    elif parts[0] == 'gtri':
        return (OPCODE_GTRI, int(parts[1]), int(parts[2]), int(parts[3]))
    elif parts[0] == 'gtrr':
        return (OPCODE_GTRR, int(parts[1]), int(parts[2]), int(parts[3]))
    elif parts[0] == 'eqir':
        return (OPCODE_EQIR, int(parts[1]), int(parts[2]), int(parts[3]))
    elif parts[0] == 'eqri':
        return (OPCODE_EQRI, int(parts[1]), int(parts[2]), int(parts[3]))
    elif parts[0] == 'eqrr':
        return (OPCODE_EQRR, int(parts[1]), int(parts[2]), int(parts[3]))

    return None

def run_opcode(opcode_data):
    global in_loop
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
    registers[instruction_register] += 1
#55664760094839
    
def part1(data):
    """Solve part 1"""
    if data[0][0] == OPCODE_IP:
        global instruction_register
        instruction_register = data[0][1]
        data = data[1:]
    while registers[instruction_register] < len(data):
        run_opcode(data[registers[instruction_register]])
    return registers[0]

def part2(data):
    """Solve part 2"""
    global registers, in_loop
    registers = [1,0,0,0,0,0]
    counter = 0
    if data[0][0] == OPCODE_IP:
        global instruction_register
        instruction_register = data[0][1]
        data = data[1:]
    while registers[instruction_register] < len(data):
        counter += 1
        run_opcode(data[registers[instruction_register]])
        if counter == 30:
            goal = registers[2]

            solution = 0
            for x in range(1,goal+1):
                for y in range(1, ceil(goal/x) + 1):
                    if goal == x*y:
                        solution += y
            return solution
    return 0

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
