"""
Solution for day 25 of year 2016
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip().split(' ')
    if line[0] == 'cpy':
        return ('cpy', line[1], line[2])
    if line[0] == 'tgl':
        return ('tgl', line[1])
    elif line[0] == 'inc':
        return ('inc', line[1])
    elif line[0] == 'dec':
        return ('dec', line[1])
    elif line[0] == 'out':
        return ('out', line[1])
    elif line[0] == 'jnz':
        return ('jnz', line[1], line[2])
    else:
        print('UNKNOWN CMMAND ' + line[0])
        print(line)
        exit()

def run(data, initial_a = 0):
    result = [initial_a, 0, 0, 0]
    idx = 0

    data = [[y for y in x] for x in data]

    jnzcache = {}

    out_idx = 0

    while idx < len(data):
        cmd = data[idx]
        if cmd[0] == 'cpy':
            result[ord(cmd[2]) - 97] = getval(cmd[1], result)
        elif cmd[0] == 'out':
            val = getval(cmd[1], result)
            if val % 2 != out_idx % 2:
                return False
            elif out_idx > 1000:
                return True
            out_idx += 1
        elif cmd[0] == 'inc':
            result[ord(cmd[1]) - 97] += 1
        elif cmd[0] == 'dec':
            result[ord(cmd[1]) - 97] -= 1
        elif cmd[0] == 'tgl':
            pos = getval(cmd[1], result) + idx
            if pos < len(data):
                if len(data[pos]) == 2:
                    if data[pos][0] == 'inc':
                        data[pos][0] = 'dec'
                    else:
                        data[pos][0] = 'inc'
                else:
                    if data[pos][0] == 'jnz':
                        data[pos][0] = 'cpy'
                    else:
                        data[pos][0] = 'jnz'
        elif cmd[0] == 'jnz':
            tmp = ord(cmd[1]) - 97
            if tmp < 0:
                if tmp != -49:
                    idx += getval(cmd[2], result) - 1
            elif getval(cmd[1], result) != 0:
                if idx not in jnzcache:
                    jnzcache[idx] = []
                jnzcache[idx].append([zz for zz in result])
                if len(jnzcache[idx]) == 10:
                    vector = find_vector(jnzcache[idx])
                    if vector:
                        factor = result["abcd".find(cmd[1]) // (vector["abcd".find(cmd[1])] * -1)] - 1
                        result[0] += vector[0] * factor
                        result[1] += vector[1] * factor
                        result[2] += vector[2] * factor
                        result[3] += vector[3] * factor
                        del jnzcache[idx]
                idx += getval(cmd[2], result) - 1
            else:
                if idx in jnzcache:
                    del jnzcache[idx]

        else:
            print("UNKNOWN COMMAND: " + cmd[0])
            exit()
        idx += 1
    return result

def find_vector(data):
    result = [data[1][0] - data[0][0], data[1][1] - data[0][1], data[1][2] - data[0][2], data[1][3] - data[0][3]]
    for x in range(2, len(data)):
        if data[x][0] - data[x - 1][0] != result[0] or data[x][1] - data[x - 1][1] != result[1] or data[x][2] - data[x - 1][2] != result[2] or data[x][3] - data[x - 1][3] != result[3]:
            return None
    return result

def getval(val, result):
    if val in 'abcd':
        return result[ord(val) - 97]
    else:
        return int(val)

def lowest_integer(data):
    for x in range(1000):
        if run(data, x):
            return x
    return None

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = lowest_integer(data)

    # Part 2
    solution2 = None
    print(data)
    print(solution2)
    exit()
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

