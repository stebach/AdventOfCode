"""
Solution for day 03 of year 2017
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return int(inputdata.read().strip())

def manhattan_distance(data):
    side = 1
    while pow(side, 2) < data:
        side += 2
    if side == 1:
        return 0
    half_side = (side - 1) // 2
    return half_side + abs(((data - pow(side - 2, 2)) % (side - 1)) - half_side)

def get_first_over(num):
    x = 0
    y = 0
    width = 1
    height = 1
    data = [
        [1]
    ]
    while data[y][x] <= num:
        if x + 1 == width and y + 1 == height:
            new_data = [[0] * (width + 2)]
            for row in data:
                new_data += [[0] + row + [0]]
            new_data += [[0] * (width + 2)]
            data = new_data
            width += 2
            height += 2
            x = width - 1
            y = height - 2
        elif y == height - 1:
            x += 1
        elif x == 0:
            y += 1
        elif y == 0:
            x -= 1
        else:
            y -= 1

        data[y][x] = get_surrounding(data, x, y)
    return data[y][x]

def get_surrounding(data, x, y):
    directions = [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]
    result = 0
    for direction in directions:
        if len(data) > y + direction[1] and y + direction[1] >= 0:
            if len(data[y + direction[1]]) > x + direction[0] and x + direction[0] >= 0:
                result += data[y + direction[1]][x + direction[0]]
    return result
            

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = manhattan_distance(data)

    # Part 2
    solution2 = get_first_over(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

