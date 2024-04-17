"""
Solution for day 08 of year 2022
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip()
    return tuple([int(x) for x in [*line]])

def visible_trees(data):
    width = len(data[0])
    height = len(data)
    visible = 0
    for y in range(height):
        for x in range(width):
            if only_smaller_trees(x,y,0,-1,data) or only_smaller_trees(x,y,0,1,data) or only_smaller_trees(x,y,-1,0,data) or only_smaller_trees(x,y,1,0,data):
                visible += 1
    return visible

def only_smaller_trees(x, y, x_change, y_change, data):
    yy = y + y_change
    xx = x + x_change
    size = data[y][x]
    while yy < len(data) and yy > -1 and xx < len(data[0]) and xx > -1:
        if data[yy][xx] >= size:
            return False
        xx += x_change
        yy += y_change
    return True


def scenic_score(data):
    width = len(data[0])
    height = len(data)
    scores = []
    for y in range(height):
        for x in range(width):
            scores.append(get_viewing_distance(x,y,0,-1,data) * get_viewing_distance(x,y,1,0,data) * get_viewing_distance(x,y,0,1,data) * get_viewing_distance(x,y,-1,0,data))
    return max(scores)

def get_viewing_distance(x, y, x_change, y_change, data):
    yy = y + y_change
    xx = x + x_change
    size = data[y][x]
    distance = 0
    while yy < len(data) and yy > -1 and xx < len(data[0]) and xx > -1:
        distance += 1
        if data[yy][xx] >= size:
            return distance
        xx += x_change
        yy += y_change
    return distance

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = visible_trees(data)

    # Part 2
    solution2 = scenic_score(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
