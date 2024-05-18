"""
Solution for day 20 of year 2015
"""

import os
import math
import time

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: int(line.strip()), inputdata.readlines()))

def get_lowest_house(data, part2 = False, modulo = 2*3*5*7):
    for check in range(10_000_000):
        if check % modulo == 0:
            if get_delivered_gifts(check) >= data:
                if part2: 
                    for check2 in range(check, 10_000_000):
                        if check2 % modulo == 0:
                            if get_delivered_gifts(check2, part2) >= data:
                                return check2
                return check

def get_delivered_gifts(data, part2 = False):
    if not part2:
        factors = get_factors(data)
        factors_set = set(factors)
        delivered_gifts = 1
        for factor in factors_set:
            add = 1
            for y in range(sum([1 for x in factors if x == factor])):
                add += pow(factor, y+1)
            delivered_gifts *= add
        return delivered_gifts * 10
    return sum(get_divisors50(data)) * 11

def get_divisors50(number):
    divisors = []
    for divisor in range(1, 51):
        if number % divisor == 0:
            divisors.append(number//divisor)
    return divisors

def get_factors(number):
    factor = 2
    factors = []
    while number > 1:
        if number % factor == 0:
            factors.append(factor)
            number //= factor
        else:
            factor += 1
    return sorted(factors)

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_lowest_house(data[0])

    # Part 2
    solution2 = get_lowest_house(data[0], True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
