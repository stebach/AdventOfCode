"""
Solution for day 11 of year 2017
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines()[0].strip())

def parse_lines(lines):
    return lines.split(',')

def get_distance(data, get_furthest = False):
    x = 0
    y = 0
    z = 0
    furthest = 0
    for step in data:
        if step == 'n':
            y += 1
            z -= 1
        elif step == 's':
            y -= 1
            z += 1
        elif step == 'ne':
            x += 1
            z -= 1
        elif step == 'sw':
            x -= 1
            z += 1
        elif step == 'se':
            x += 1
            y -= 1
        elif step == 'nw':
            x -= 1
            y += 1
        else:
            print("unknown direction: " + step)
            exit()
        if get_furthest:
            check =  (abs(x) + abs(y) + abs(z)) // 2
            if check > furthest:
                furthest = check
    if get_furthest:
        return furthest
    return (abs(x) + abs(y) + abs(z)) // 2

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_distance(data)

    # Part 2
    solution2 = get_distance(data, True)
    print(data)
    print(solution2)
    exit()
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

