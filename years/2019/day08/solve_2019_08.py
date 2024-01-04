"""
Solution for day 08 of year 2019
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_line(inputdata.read())

def parse_line(line):
    line = line.strip()
    return tuple([tuple([int(y) for y in [* line][x:x+150]]) for x in range(0, len(line), 25*6)])


def part1(data):
    """Solve part 1"""
    min_0 = 1000
    result = 0
    for layer in data:
        if layer.count(0) < min_0:
            min_0 = layer.count(0)
            result = layer.count(1) * layer.count(2)
    return result

def part2(data):
    """Solve part 2"""
    layer = [0] * 150
    for x in range(len(data)):
        for y in range(150):
            z = data[len(data)-1-x][y]
            if z != 2:
                layer[y] = z

    output = ''
    for x in range(0,150,25):
        row = layer[x:x+25]
        for pos in row:
            if pos == 0:
                output += ' '
            else:
                output += '█'
        output += '\n'
    return output



def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
