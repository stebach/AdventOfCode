"""
Solution for day 18 of year 2015
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = []
    for (y, line) in enumerate(lines):
        for (x, char) in enumerate(line.strip()):
            if char == '#':
                result.append((x, y))
    return (len(lines), len(lines[0].strip()), set(result))

def animate(data, amount, fixed_corners = False):
    lights = data[2]
    adjacent = ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1))
    if fixed_corners:
        lights.add((0,0))
        lights.add((0,data[1]-1))
        lights.add((data[0]-1,0))
        lights.add((data[0]-1,data[1]-1))
    for run in range(amount):
        new_lights = set()
        for y in range(data[0]):
            for x in range(data[1]):
                adjacent_on = len([a for a in adjacent if (a[0] + x, a[1] + y) in lights])
                if (x,y) in lights and adjacent_on in (2, 3):
                    new_lights.add((x,y))
                elif (x,y) not in lights and adjacent_on == 3:
                    new_lights.add((x,y))
        if fixed_corners:
            new_lights.add((0,0))
            new_lights.add((0,data[1]-1))
            new_lights.add((data[0]-1,0))
            new_lights.add((data[0]-1,data[1]-1))
        lights = new_lights
    return lights

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = len(animate(data, 100))

    # Part 2
    solution2 =  len(animate(data, 100, True))

    print(solution2)
    exit()
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
