"""
Solution for day 18 of year 2017
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip().split(' ')
    result = [line[0], line[1]]
    if line[0] in ['set','add','mul','mod','jgz']:
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

def recover(data):
    registers = {}
    idx = 0
    running = True
    
    sound = 0

    while running:
        if data[idx][0] == 'set':
            if data[idx][2] == 'n':
                registers[data[idx][1]] = data[idx][3]
            else:
                registers[data[idx][1]] = getRegisterValue(registers, data[idx][3])
        elif data[idx][0] == 'add':
            if not data[idx][1] in registers:
                registers[data[idx][1]] = 0
            if data[idx][2] == 'n':
                registers[data[idx][1]] += data[idx][3]
            else:
                registers[data[idx][1]] += getRegisterValue(registers, data[idx][3])
        elif data[idx][0] == 'mul':
            if not data[idx][1] in registers:
                registers[data[idx][1]] = 0
            if data[idx][2] == 'n':
                registers[data[idx][1]] *= data[idx][3]
            else:
                registers[data[idx][1]] *= getRegisterValue(registers, data[idx][3])
        elif data[idx][0] == 'mod':
            if not data[idx][1] in registers:
                registers[data[idx][1]] = 0
            if data[idx][2] == 'n':
                registers[data[idx][1]] = registers[data[idx][1]] % data[idx][3]
            else:
                registers[data[idx][1]] = registers[data[idx][1]] % getRegisterValue(registers, data[idx][3])
        elif data[idx][0] == 'jgz':
            check = 0
            try:
                check = int(data[idx][1])
            except ValueError:
                check = registers[data[idx][1]]

            if check > 0:
                if data[idx][2] == 'n':
                    idx += data[idx][3] - 1
                else:
                    idx += getRegisterValue(registers, data[idx][3]) - 1
        elif data[idx][0] == 'snd':
            sound = getRegisterValue(registers, data[idx][1])
        elif data[idx][0] == 'rcv':
            if data[idx][1] != '0':
                return sound
        else:
            print("UNKNOWN: " + data[idx][0])
            exit()
        idx += 1

def getRegisterValue(registers, key):
    if key in registers:
        return registers[key]
    return 0

def count_sends(data, program):
    registers = [{'p':0},{'p':1}]
    idx = [0,0]
    program_running = 0
    sent_data = [[],[]]
    rcv_index = [0,0]
    running = True

    while running:
        if data[idx[program_running]][0] == 'set':
            if data[idx[program_running]][2] == 'n':
                registers[program_running][data[idx[program_running]][1]] = data[idx[program_running]][3]
            else:
                registers[program_running][data[idx[program_running]][1]] = getRegisterValue(registers[program_running], data[idx[program_running]][3])
        elif data[idx[program_running]][0] == 'add':
            if not data[idx[program_running]][1] in registers[program_running]:
                registers[program_running][data[idx[program_running]][1]] = 0
            if data[idx[program_running]][2] == 'n':
                registers[program_running][data[idx[program_running]][1]] += data[idx[program_running]][3]
            else:
                registers[program_running][data[idx[program_running]][1]] += getRegisterValue(registers[program_running], data[idx[program_running]][3])
        elif data[idx[program_running]][0] == 'mul':
            if not data[idx[program_running]][1] in registers[program_running]:
                registers[program_running][data[idx[program_running]][1]] = 0
            if data[idx[program_running]][2] == 'n':
                registers[program_running][data[idx[program_running]][1]] *= data[idx[program_running]][3]
            else:
                registers[program_running][data[idx[program_running]][1]] *= getRegisterValue(registers[program_running], data[idx[program_running]][3])
        elif data[idx[program_running]][0] == 'mod':
            if not data[idx[program_running]][1] in registers[program_running]:
                registers[program_running][data[idx[program_running]][1]] = 0
            if data[idx[program_running]][2] == 'n':
                registers[program_running][data[idx[program_running]][1]] = registers[program_running][data[idx[program_running]][1]] % data[idx[program_running]][3]
            else:
                registers[program_running][data[idx[program_running]][1]] = registers[program_running][data[idx[program_running]][1]] % getRegisterValue(registers[program_running], data[idx[program_running]][3])
        elif data[idx[program_running]][0] == 'jgz':
            check = 0
            try:
                check = int(data[idx[program_running]][1])
            except ValueError:
                check = registers[program_running][data[idx[program_running]][1]]

            if check > 0:
                if data[idx[program_running]][2] == 'n':
                    idx[program_running] += data[idx[program_running]][3] - 1
                else:
                    idx[program_running] += getRegisterValue(registers[program_running], data[idx[program_running]][3]) - 1
        elif data[idx[program_running]][0] == 'snd':
            sent_data[program_running].append(getRegisterValue(registers[program_running], data[idx[program_running]][1]))
        elif data[idx[program_running]][0] == 'rcv':
            if data[idx[program_running]][1] != '0':
                if len(sent_data[(program_running + 1) % 2]) > rcv_index[program_running]:
                    registers[program_running][data[idx[program_running]][1]] = sent_data[(program_running + 1) % 2][rcv_index[program_running]]
                    rcv_index[program_running] += 1
                elif data[idx[(program_running + 1) % 2]][0] == 'rcv' and len(sent_data[program_running]) <= rcv_index[(program_running + 1) % 2]:
                    return len(sent_data[program])
                else:
                    program_running = (program_running + 1) % 2
                    idx[program_running] -= 1
        else:
            print("UNKNOWN: " + data[idx[program_running]][0])
            exit()
        idx[program_running] += 1


def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = recover(data)

    # Part 2
    solution2 = count_sends(data, 1)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
