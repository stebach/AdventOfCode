"""
Solution for day 17 of year 2015
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: int(line.strip()), inputdata.readlines()))

def get_combinations(data, amount, current = []):
    result = []

    if len(data) > 0:
        nextnum = data[0]
        if amount - nextnum == 0:
            result.append(current + [nextnum])
        elif amount - nextnum > 0:
            result += get_combinations(data[1:], amount - nextnum, current + [nextnum])
        result += get_combinations(data[1:], amount, current)

    return result

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    combinations = get_combinations(data, 150)
    solution1 = len(combinations)

    # Part 2
    numbers = [len(x) for x in combinations]
    solution2 = len([x for x in numbers if x == min(numbers)])

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
