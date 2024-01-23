"""
Solution for day 04 of year 2020
"""

import os
import regex

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    lines += ['']
    passports = []
    passport = {}
    int_attrs = ['eyr','byr','iyr','cid']
    for line in lines:
        line = line.strip()
        if line == '' and passport != {}:
            passports.append(passport)
            passport = {}
        elif line != '':
            parts = line.split(" ")
            for part in parts:
                attr = part.split(':')
                passport[attr[0]] = attr[1] if attr[0] not in int_attrs else int(attr[1])

    return tuple(passports)

def is_valid(passport):
    return len(passport) == 8 or (len(passport) == 7 and 'cid' not in passport)

def is_valid_strict(password):
    return (
        is_valid(password)
        and password['byr'] >= 1920
        and password['byr'] <= 2002
        and password['iyr'] >= 2010
        and password['iyr'] <= 2020
        and password['eyr'] >= 2020
        and password['eyr'] <= 2030
        and valid_height(password['hgt'])
        and regex.match('^#[0-9a-f]{6}$',password['hcl']) != None
        and password['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']
        and regex.match('^[0-9]{9}$',password['pid']) != None
    )

def valid_height(height):
    if height[-2:] == 'cm':
        cm = int(height[0:-2])
        return cm >= 150 and cm <= 193
    elif height[-2:] == 'in':
        inch = int(height[0:-2])
        return inch >= 59 and inch <= 76
    return False

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = sum([is_valid(x) for x in data])

    # Part 2
    solution2 =  sum([is_valid_strict(x) for x in data])
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

