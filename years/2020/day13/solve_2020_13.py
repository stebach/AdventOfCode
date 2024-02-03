"""
Solution for day 13 of year 2020
"""

import os
import z3
from functools import reduce

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    return (
        int(lines[0]),
        [-1 if x == 'x' else int(x) for x in lines[1].strip().split(',')]
    )

def get_earliest(data):
    retval = 0
    mindepart = data[0] * 1000
    for x in data[1]:
        if x == -1:
            continue
        depart = data[0] + (x - (data[0] % x))
        if depart < mindepart:
            mindepart = depart
            retval = x * (x - (data[0] % x))
    return retval

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def mod_inverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
 
def get_earliest_with_offsets(data):
    # CRT - Chinese Remainder Theorem
    data = [x for x in enumerate(data[1]) if x[1] > -1]
    product = reduce(lambda y,z: y*z, [x[1] for x in data])
    result = 0

    for x in data:
        num = product // x[1]
        inverse = mod_inverse(num, x[1])
        result += x[0] * inverse * num
    
    return product - (result % product)

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_earliest(data)

    # Part 2
    solution2 = get_earliest_with_offsets(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
