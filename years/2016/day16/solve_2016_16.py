"""
Solution for day 16 of year 2016
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return inputdata.read().strip()

def dragon_curve(data):
    return data + "0" + "".join([str((int(x) + 1) % 2) for x in [*data[::-1]]])

def checksum(data, size):
    result = "".join(["1" if data[x*2:x*2+2] in ("11","00") else "0" for x in range(min(size // 2, len(data) // 2))])
    if len(result) % 2 == 0:
        return checksum(result, size)
    return result

def checksum_for_disk(data, size):
    while len(data) < size:
        data = dragon_curve(data)
    return checksum(data, size)

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = checksum_for_disk(data, 272)
    # Part 2
    solution2 = checksum_for_disk(data, 35651584)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
