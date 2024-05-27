"""
Solution for day 08 of year 2016
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip().split(' ')
    if line[0] == 'rect':
        return tuple([line[0]] + [int(x) for x in line[1].split('x')])
    elif line[0] == 'rotate':
        return (line[0], 1 if line[1] == 'column' else 0, int(line[2][2:]), int(line[4]))
    else:
        print('UNKNOWN OPERATION:')
        print(line)
        exit()

def count_lit(data):
    return sum([x[1] * x[2] for x in data if x[0] == 'rect'])

def draw(data, cols=50, rows=6):
    lit = []
    for o in data:
        if o[0] == 'rect':
            for x in range(o[1]):
                for y in range(o[2]):
                    if [x,y] not in lit:
                        lit.append([x,y])
        elif o[0] == 'rotate':
            if o[1] == 1:
                lit = [[x[0], (x[1] + (o[3] if x[0] == o[2] else 0)) % rows] for x in lit]
            else:
                lit = [[(x[0] + (o[3] if x[1] == o[2] else 0)) % cols, x[1]] for x in lit]
    return grid_to_string(lit, cols, rows)

def grid_to_string(data, cols, rows):
    result = ''
    for y in range(rows):
        for x in range(cols):
            if [x,y] in data:
                result += '█'
            else:
                result += ' '
        if y + 1 < rows:
            result += '\n'
    return result


def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = count_lit(data)

    # Part 2
    solution2 = draw(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
