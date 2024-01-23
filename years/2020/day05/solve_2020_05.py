"""
Solution for day 05 of year 2020
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: line.strip(), inputdata.readlines()))

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    ids = [decode_seat(x)[2] for x in data]
    solution1 = max(ids)

    # Part 2
    for x in range(solution1):
        if x not in ids and x + 1 in ids and x -1 in ids:
            solution2 = x
            break

    return solution1, solution2

def decode_seat(encoded):
    row = int(encoded[0:7].replace('B','1').replace('F','0'),2)
    col = int(encoded[7:10].replace('R','1').replace('L','0'),2)
    return (row, col, row * 8 + col)

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

