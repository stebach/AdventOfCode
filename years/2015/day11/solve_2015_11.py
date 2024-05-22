"""
Solution for day 11 of year 2015
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return inputdata.read().strip()

def string_to_password(data):
    return [ord(x) for x in data]

def password_to_string(data):
    return "".join([chr(x) for x in data])

def increment_password(data):
    pos = 1
    data[-pos] += 1
    while data[-pos] > 122:
        data[-pos] = 97
        pos += 1
        data[-pos] += 1
    return data

def validate_increasing_straight(data):
    for pos in range(5):
        if data[pos + 1] == data[pos] + 1 and data[pos + 2] == data[pos] + 2:
            return True
    return False

def validate_no_forbidden_letters(data):
    return 105 not in data and 111 not in data and 108 not in data

def validate_two_pairs(data):
    pairs = []
    for x in range(7):
        if data[x] == data[x + 1]:
            pairs.append(x)
    for pair1 in range(0, len(pairs) -1):
        for pair2 in range(pair1, len(pairs)):
            if abs(pairs[pair2] - pairs[pair1]) > 1:
                return True
    return False

def validate_password(data):
    return validate_no_forbidden_letters(data) and validate_increasing_straight(data) and validate_two_pairs(data)

def find_next_valid_password(data):
    next_password = increment_password(data)
    while not validate_password(next_password):
        next_password = increment_password(next_password)
    return next_password

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = password_to_string(find_next_valid_password(string_to_password(data)))

    # Part 2
    solution2 = password_to_string(find_next_valid_password(string_to_password(solution1)))

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))


