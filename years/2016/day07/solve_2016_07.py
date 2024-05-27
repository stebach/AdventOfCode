"""
Solution for day 07 of year 2016
"""

import os
import regex

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: line.strip(), inputdata.readlines()))

def abba_outside_brackets(data):
    return find_abba(data, True)

def abba_inside_brackets(data):
    return find_abba(data, False)

def find_abba(data, outside):
    data = data.replace('[',']').split(']')
    for x in range(0 if outside else 1, len(data), 2):
        if regex.search(r'(.)(?!\1)(.)\2\1', data[x]):
            return True
    return False

def supports_tls(data):
    return abba_outside_brackets(data) and not abba_inside_brackets(data)

def supports_ssl(data):
    data = data.replace('[',']').split(']')
    result = [[], []]
    for x in range(0, len(data)):
        for y in regex.findall(r'(.)(?!\1)(.)\1', data[x], overlapped=True):
            result[x%2].append(y[x%2] + y[(x+1)%2])
    return len([x for x in result[0] if x in result[1]]) > 0

def solve(data):
    """Solve the puzzle or the given input"""
    # Part 1
    solution1 = sum([supports_tls(x) for x in data])

    # Part 2
    solution2 = sum([supports_ssl(x) for x in data])
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
