"""
Solution for day 05 of year 2016
"""

import os
import hashlib

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return inputdata.read().strip()

def find_password(data):
    password = ''
    password2 = ['','','','','','','','']
    idx = 0
    while password2.count('') > 0:
        hash = hashlib.md5((data + str(idx)).encode('utf-8')).hexdigest()
        if hash[0:5] == '00000':
            password += hash[5]
            position = int(hash[5], 16)
            if position < 8 and password2[position] == '':
                password2[position] = hash[6]
        idx += 1
    return (password[0:8], "".join(password2))

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    passwords = find_password(data)
    solution1 = passwords[0]

    # Part 2
    solution2 = passwords[1]

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
