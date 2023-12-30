"""
Solution for day 23 of year 2018
"""

import os
import z3

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    tmp = line.strip().split(', r=')
    return tuple([int(x) for x in tmp[0][5:-1].split(',')] + [int(tmp[1])])

def part1(data):
    """Solve part 1"""
    max_range_bot = [y for y in data if y[3] == max([x[3] for x in data])][0]
    in_range = [x for x in data if abs(x[0] - max_range_bot[0]) + abs(x[1] - max_range_bot[1]) + abs(x[2] - max_range_bot[2]) <= max_range_bot[3]]
    return len(in_range)

def zabs(x):
    return z3.If(x < 0, -x, x)

def part2(data):
    """Solve part 2"""
    opt = z3.Optimize()
    x = z3.Int('x')
    y = z3.Int('y')
    z = z3.Int('z')
    in_range = [z3.Int(f'bot_{i}') for i in range(len(data))]
    for i in range(len(data)):
        opt.add(in_range[i] == z3.If(zabs(x - data[i][0]) + zabs(y - data[i][1]) + zabs(z - data[i][2]) <= data[i][3], 1, 0))
    count = z3.Int('count')
    opt.add(count == sum(in_range))
    opt.maximize(count)
    to_center = z3.Int('to_center')
    opt.add(to_center == zabs(x) + zabs(y) + zabs(z))
    opt.minimize(to_center)
    
    if opt.check() == z3.sat:
        model = opt.model()
        return model[to_center]

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
