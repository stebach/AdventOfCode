"""
Solution for day 23 of year 2017
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip().split(' ')
    result = [line[0], line[1]]
    if line[0] in ['set','add','mul','mod','jnz','sub']:
        try:
            number = int(line[2])
            result.append('n')
            result.append(number)
        except ValueError:
            result.append('r')
            result.append(line[2])
    elif line[0] not in ['snd','rcv']:
        print("UNKNOWN: " + line[0])
        exit()
    return tuple(result)

def getRegisterValue(registers, key):
    if key in registers:
        return registers[key]
    return 0

def count_mul(data, a_start = None):
    registers = {}
    if a_start:
        # rewritten input:
        h = 0
        for b in range(106500, 123501, 17):
            if not prime(b):
                h += 1
        return h
    idx = 0
    running = True
    mul_count = 0

    while running:
        if idx >= len(data):
            if a_start != None:
                return registers
            return mul_count
        if data[idx][0] == 'set':
            if data[idx][2] == 'n':
                registers[data[idx][1]] = data[idx][3]
            else:
                registers[data[idx][1]] = getRegisterValue(registers, data[idx][3])
        elif data[idx][0] == 'sub':
            if not data[idx][1] in registers:
                registers[data[idx][1]] = 0
            if data[idx][2] == 'n':
                registers[data[idx][1]] -= data[idx][3]
            else:
                registers[data[idx][1]] -= getRegisterValue(registers, data[idx][3])
        elif data[idx][0] == 'mul':
            mul_count += 1
            if not data[idx][1] in registers:
                registers[data[idx][1]] = 0
            if data[idx][2] == 'n':
                registers[data[idx][1]] *= data[idx][3]
            else:
                registers[data[idx][1]] *= getRegisterValue(registers, data[idx][3])
        elif data[idx][0] == 'jnz':
            check = 0
            try:
                check = int(data[idx][1])
            except ValueError:
                check = getRegisterValue(registers, data[idx][1])

            if check != 0:
                if data[idx][2] == 'n':
                    idx += data[idx][3] - 1
                else:
                    idx += getRegisterValue(registers, data[idx][3]) - 1
        else:
            print("UNKNOWNxx: \"" + data[idx][0] + "\"")
            exit()
        idx += 1

def prime(num):
    for i in range(2, (num//2)+1):
        if (num % i) == 0:
            return False
    return True

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = count_mul(data)

    # Part 2
    solution2 = count_mul(data, 1)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
