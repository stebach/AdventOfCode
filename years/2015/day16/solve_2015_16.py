"""
Solution for day 16 of year 2015
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip()[4:].split(': ',1)
    return ((int(line[0]), dict([[y[0], int(y[1])] for y in [x.split(': ') for x in line[1].split(', ')]])))

def find_valid_entries(data, use_ranges = False):
    result = []
    for entry in data:
        valid = True
        for key in entry[1]:
            if key == 'children' and entry[1][key] != 3:
                valid = False
                break
            if (key == 'cats' and entry[1][key] != 7 and use_ranges is False):
                valid = False
                break
            if (key == 'cats' and entry[1][key] <= 7 and use_ranges is True):
                valid = False
                break
            if key == 'samoyeds' and entry[1][key] != 2:
                valid = False
                break
            if (key == 'pomeranians' and entry[1][key] != 3 and use_ranges is False):
                valid = False
                break
            if (key == 'pomeranians' and entry[1][key] >= 3 and use_ranges is True):
                valid = False
                break
            if key == 'akitas' and entry[1][key] != 0:
                valid = False
                break
            if key == 'vizslas' and entry[1][key] != 0:
                valid = False
                break
            if (key == 'goldfish' and entry[1][key] != 5 and use_ranges is False):
                valid = False
                break
            if (key == 'goldfish' and entry[1][key] >= 5 and use_ranges is True):
                valid = False
                break
            if (key == 'trees' and entry[1][key] != 3 and use_ranges is False):
                valid = False
                break
            if (key == 'trees' and entry[1][key] <= 3 and use_ranges is True):
                valid = False
                break
            if key == 'cars' and entry[1][key] != 2:
                valid = False
                break
            if key == 'perfumes' and entry[1][key] != 1:
                valid = False
                break
        if valid:
            result.append(entry[0])
    return result

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = find_valid_entries(data)[0]

    # Part 2
    solution2 = find_valid_entries(data, True)[0]

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

