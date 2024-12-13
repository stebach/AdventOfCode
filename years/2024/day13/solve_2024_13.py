"""
Solution for day 13 of year 2024
"""

import os
import z3

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = [{}]

    for line in lines:
        if line[0:7] == 'Button ':
            result[-1][line[7]] = {
                'X': int(line[9:].split(', ')[0][2:]),
                'Y': int(line[9:].split(', ')[1][2:])
            }
        elif line[0:6] == 'Prize:':
            result[-1]['Prize'] = {
                'X': int(line[7:].split(', ')[0][2:]),
                'Y': int(line[7:].split(', ')[1][2:])
            }
            result.append({})

    return tuple(result[:-1])

def cheepest(data, cost_a, cost_b, higher = False):
    opt = z3.Optimize()
    cost = z3.Int('cost')
    a = z3.Int('a')
    b = z3.Int('b')
    opt.add(cost == a * cost_a + b * cost_b)
    to_add = 0
    if higher:
        to_add = 10000000000000
    opt.add(data['Prize']['X'] + to_add == a * data['A']['X'] + b * data['B']['X'])
    opt.add(data['Prize']['Y'] + to_add == a * data['A']['Y'] + b * data['B']['Y'])
    if not higher:
        opt.add(a <= 100)
        opt.add(b <= 100)
    opt.minimize(cost)

    if opt.check() == z3.sat:
        model = opt.model()
        return model[cost].as_long()

    return 0

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = sum([cheepest(x, 3, 1) for x in data])

    # Part 2
    solution2 = sum([cheepest(x, 3, 1, True) for x in data])

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

