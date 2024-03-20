"""
Solution for day 17 of year 2020
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())


def parse_lines(lines):
    res = []
    for y, line in enumerate(lines):
        line = line.strip()
        for x, char in enumerate(line):
            if char == '#':
                res.append((x, y, 0, 0))
    return tuple(res)

def run_cycles(data, cycles, four_dimensions = False):
    for cycle in range(cycles):
        new_data = []
        data_x = [x[0] for x in data]
        data_y = [x[1] for x in data]
        data_z = [x[2] for x in data]
        data_w = [x[3] for x in data]
        data_min = [min(data_x)-1, min(data_y)-1, min(data_z)-1, min(data_w)-1 if four_dimensions else 0]
        data_max = [max(data_x)+2, max(data_y)+2, max(data_z)+2, max(data_w)+2 if four_dimensions else 1]

        for x in range(data_min[0], data_max[0]):
            for y in range(data_min[1], data_max[1]):
                for z in range(data_min[2], data_max[2]):
                    for w in range(data_min[3], data_max[3]):
                        c = len([a for a in data if abs(a[0]-x) < 2 and abs(a[1]-y) < 2 and abs(a[2]-z) < 2 and abs(a[3]-w) < 2])
                        if ((x,y,z,w) in data and c in (3,4)) or ((x,y,z,w) not in data and c == 3):
                            new_data.append((x,y,z,w))
        data = new_data

    return len(data)

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = run_cycles(data, 6)
    # Part 2
    solution2 = run_cycles(data, 6, True)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
