"""
Solution for day 24 of year 2015
"""

import os
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: int(line.strip()), inputdata.readlines()))

def get_lowest_quantum_entanglement(data, groups = 3):
    target = sum(data) // groups
    numbers = sorted(data, reverse=True)
    combinations = get_combinations(numbers, target)
    smallest_amount = min([len(x) for x in combinations])
    return min([quantum_entanglement(x) for x in combinations if len(x) == smallest_amount])

def quantum_entanglement(data):
    result = 1
    for x in data:
        result *= x
    return result

def get_combinations(numbers, target, group = []):
    result = []
    next_number = numbers[0]
    if sum(group) + next_number < target and len(numbers) > 1:
        result += get_combinations(numbers[1:], target, group + [next_number])
    elif sum(group) + next_number == target:
        result += [group + [next_number]]
    if len(numbers) > 1:
        result += get_combinations(numbers[1:], target, group)
    return result
        

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_lowest_quantum_entanglement(data)

    # Part 2
    solution2 = get_lowest_quantum_entanglement(data, 4)
    print(solution2)
    exit()
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

