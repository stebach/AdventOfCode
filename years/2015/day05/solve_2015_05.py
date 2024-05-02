"""
Solution for day 05 of year 2015
"""

import os
import regex

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: line.strip(), inputdata.readlines()))

def three_vowels(data):
    return len([x for x in data if x in 'aeiou']) > 2

def one_letter_twice(data):
    return len([x for x in enumerate(data) if x[0] > 0 and x[1] == data[x[0]-1]]) > 0

def does_not_contain_forbidden_strings(data):
    return 'ab' not in data and 'cd' not in data and 'pq' not in data and 'xy' not in data

def is_nice(data):
    return three_vowels(data) and one_letter_twice(data) and does_not_contain_forbidden_strings(data)

def count_nice(data):
    return len([x for x in data if is_nice(x)])

def two_letters_twice(data):
    return regex.match(r".*(.{2}).*\1", data) is not None

def one_letter_twice_with_one_between(data):
    return regex.match(r".*(.).\1", data) is not None

def is_nice2(data):
    return two_letters_twice(data) and one_letter_twice_with_one_between(data)
    

def count_nice2(data):
    return len([x for x in data if is_nice2(x)])


def solve(data):
    # Part 1
    solution1 = count_nice(data)

    # Part 2
    solution2 = count_nice2(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

