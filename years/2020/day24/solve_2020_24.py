"""
Solution for day 24 of year 2020
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:

        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip()
    x = 0
    y = 0
    chars = [*line]
    #e 1,0
    #w -1, 0
    #nw -1, -1
    #ne 0, -1
    #sw 0, 1
    #se 1, 1
    while len(chars) > 0:
        char = chars.pop(0)
        if char == "s":
            y += 1
            char = chars.pop(0)
            if char == "e":
                x += 1
        elif char == "n":
            y -= 1
            char = chars.pop(0)
            if char == "w":
                x -= 1
        elif char == "e":
            x += 1
        elif char == "w":
            x -= 1
    return (x,y)

def toggle(data, entry):
    if entry in data:
        data.remove(entry)
    else:
        data.append(entry)

def flip(black):
    x_list = [x[0] for x in black]
    y_list = [x[1] for x in black]
    min_x = min(x_list)
    max_x = max(x_list)
    min_y = min(y_list)
    max_y = max(y_list)

    new_black = []

    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            adjacent_black = sum([
                1 if (x+1,y) in black else 0, #e
                1 if (x-1,y) in black else 0, #w
                1 if (x-1,y-1) in black else 0, #nw
                1 if (x,y-1) in black else 0, #ne
                1 if (x,y+1) in black else 0, #sw
                1 if (x+1,y+1) in black else 0, #se
            ])
            if ((x,y) in black and adjacent_black in [1,2]) or ((x,y) not in black and adjacent_black == 2):
                new_black.append((x,y))
    return new_black

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    black = []
    for entry in data:
        toggle(black, entry)
    solution1 = len(black)

    # Part 2
    for flipcount in range(100):
        black = flip(black)
    solution2 = len(black)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
