"""
Solution for day 25 of year 2024
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    keys = []
    locks = []

    i = 0
    while i < len(lines):
        value = [-1, -1, -1, -1, -1]
        for check in range(7):
            for pos in range(5):
                value[pos] += 1 if lines[i + check][pos] == '#' else 0
        
        if lines[i].strip() == '.....':
            keys.append(tuple(value))
        else:
            locks.append(tuple(value))

        i += 8

    return {
        'locks': tuple(locks),
        'keys': tuple(keys)
    }

def get_fitting_pair_count(data):
    count = 0
    for lock in data['locks']:
        for key in data['keys']:
            if max([lock[i] + key[i] for i in range(5)]) < 6:
                count += 1
    return count

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_fitting_pair_count(data)
    print(data)
    print(solution1)

    return solution1, None

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

