"""
Solution for day 14 of year 2020
"""

import os
import regex

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip()
    if line[0:7] == 'mask = ':
        return ('mask', line[7:])
    else:
        check = regex.findall('^mem\\[([0-9]+)\\] = ([0-9]+)$', line)
        if len(check) > 0:
            return ('mem', int(check[0][0]), int(check[0][1]))
    print(line)
    exit()

def initialize(data):
    map = {}
    andmask = 0
    ormask = 0
    for x in data:
        if x[0] == 'mask':
            ormask = int(x[1].replace('X','0'),2)
            andmask = int(x[1].replace('X','1'),2)
        else:
            map[x[1]] = x[2] & andmask | ormask
    return sum([map[x] for x in map])

def initialize2(data):
    map = {}
    ormask = 0
    xpos = []
    for x in data:
        if x[0] == 'mask':
            ormask = int(x[1].replace('X','0'),2)
            xpos = [y.start() for y in regex.finditer('X', x[1])]
        else:
            addresses = [x[1] | ormask]
            for pos in xpos:
                ormask2 = int(('0' * pos) + '1' + ('0' * (36 - pos - 1)), 2)
                andmask2 = int(('1' * pos) + '0' + ('1' * (36 - pos - 1)), 2)
                new_addresses = []
                for a in addresses:
                    new_addresses += [a & andmask2]
                    new_addresses += [a | ormask2]
                addresses = new_addresses
            for pos in addresses:
                map[pos] = x[2]

    return sum([map[x] for x in map])

def parse_lines(lines):
    return [x for x in lines]

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = initialize(data)

    # Part 2
    solution2 = initialize2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
