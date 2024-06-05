"""
Solution for day 15 of year 2016
"""

import os
import z3

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip()[:-1].split(' ')
    return (int(line[3]), int(line[-1]))

def find_time(data):
    opt = z3.Optimize()
    time = z3.Int('time')
    for pos, row in enumerate(data):
        tmp = z3.Int('x' + str(pos))
        opt.add(tmp == row[1])
        opt.add((tmp + time + pos + 1) % row[0] == 0)
    opt.add(time >= 0)
    opt.minimize(time)
    if opt.check() == z3.sat:
        model = opt.model()
        return model[time]
    else:
        print("NO SOLUTION FOUND!")
        exit()

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = find_time(data)

    # Part 2
    solution2 = find_time(data + ((11,0),))

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
