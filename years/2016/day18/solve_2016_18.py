"""
Solution for day 18 of year 2016
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return inputdata.read().strip()

def get_safe_tiles(data, lines):
    result = [data]
    while len(result) < lines:
        result.append("".join(['^' if ((y.count('^') == 1 and y[1] != '^') or (y.count('^') == 2 and y[1] == '^')) else '.' for y in [[('.' + result[-1] + '.')[x-1],('.' + result[-1] + '.')[x],('.' + result[-1] + '.')[x+1]] for x in range(1,len(data) + 1)]]))
    return "".join(result).count('.')

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_safe_tiles(data, 40)

    # Part 2
    solution2 = get_safe_tiles(data, 400000)
    print(solution2)
    exit()
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

