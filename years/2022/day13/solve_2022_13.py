"""
Solution for day 13 of year 2022
"""

import os
from json import loads
from functools import cmp_to_key

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = []
    while len(lines) > 0:
        line = lines.pop(0).strip()
        if len(line) == 0:
            continue
        result.append([
            loads(line),
            loads(lines.pop(0).strip())
        ])
    return result

def right_order(data):
    result = []
    for (idx, items) in enumerate(data):
        if compare(items[0], items[1]) == -1:
            result.append(idx + 1)
    return result

def compare(a, b):
    a_len = len(a)
    b_len = len(b)

    for idx in range(a_len):
        if b_len <= idx:
            return 1
        if isinstance(a[idx], int) and isinstance(b[idx], int):
            if a[idx] < b[idx]:
                return -1
            if a[idx] > b[idx]:
                return 1
        else:
            sub_a = a[idx]
            if isinstance(sub_a, int):
                sub_a = [sub_a]
            sub_b = b[idx]
            if isinstance(sub_b, int):
                sub_b = [sub_b]
            subresult = compare(sub_a, sub_b)
            if subresult != 0:
                return subresult
    if b_len > a_len:
        return -1
    return 0


    return -2

def decoder_key(data):
    data_to_sort = [
        [[2]],
        [[6]]
    ]
    for pair in data:
        data_to_sort += pair
    
    data_to_sort = sorted(data_to_sort, key=cmp_to_key(compare))
    return (data_to_sort.index([[2]]) + 1) * (data_to_sort.index([[6]]) + 1)

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = sum(right_order(data))

    # Part 2
    solution2 = decoder_key(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
