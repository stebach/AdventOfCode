"""
Solution for day 10 of year 2020
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: int(line.strip()), inputdata.readlines()))

def differences_when_all_are_used(data):
    data_sorted = [0] + sorted(data) + [max(data) +3]
    result = [0,0,0]
    for i in range(1,len(data_sorted)):
        result[data_sorted[i] - data_sorted[i-1] -1] += 1
    return tuple(result)

def number_of_arrangements(data):
    data_sorted = [0] + sorted(data)
    data_sorted = data_sorted[::-1]
    arrangements = {
        (max(data) + 3): 1
    }
    for i in range(len(data_sorted)):
        num = 0
        for j in range(3):
            if data_sorted[i] + j + 1 in arrangements:
                num += arrangements[data_sorted[i] + j + 1]
        arrangements[data_sorted[i]] = num

    return arrangements[0]

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    jumps = differences_when_all_are_used(data)
    solution1 = jumps[0] * jumps[2]

    # Part 2
    solution2 = number_of_arrangements(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
