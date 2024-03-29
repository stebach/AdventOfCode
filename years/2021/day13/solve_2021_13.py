"""
Solution for day 13 of year 2021
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    coords = []
    folds = []
    while lines[0].strip() != "":
        line = lines.pop(0).strip()
        coords.append([int(x) for x in line.split(',')])
    lines.pop(0)
    while len(lines) > 0:
        line = lines.pop(0).strip()[11:].split('=')
        folds.append([line[0], int(line[1])])
    return [
        coords,
        folds
    ]

def fold(data):
    if len(data[1]) > 0:
        new_coords = []
        fold = data[1].pop(0)
        coord_pos = 0
        if fold[0] == 'y':
            coord_pos = 1
        for coord in data[0]:
            if coord[coord_pos] == fold[1]:
                continue
            elif coord[coord_pos] > fold[1]:
                coord[coord_pos] = fold[1] * 2 - coord[coord_pos]
            if coord not in new_coords:
                new_coords.append(coord)
        data[0] = new_coords
    return data

def draw(coords):
    x_coords = [x[0] for x in coords]
    y_coords = [x[1] for x in coords]

    result = ""

    for y in range(min(y_coords), max(y_coords) + 1):
        for x in range(min(x_coords), max(x_coords) + 1):
            if [x,y] in coords:
                result += "█"
            else:
                result += " "
        result += "\n"

    return result
    

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    fold(data)
    solution1 = len(data[0])

    while len(data[1]) > 0:
        fold(data)

    # Part 2
    solution2 = draw(data[0])

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
