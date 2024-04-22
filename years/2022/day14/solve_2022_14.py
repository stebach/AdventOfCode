"""
Solution for day 14 of year 2022
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = set([])
    for line in lines:
        points = [tuple([int(y) for y in x.split(',')]) for x in line.strip().split(' -> ')]
        current_point = points.pop(0)
        result.add(current_point)
        while len(points) > 0:
            next_point = points.pop(0)
            for x in range(min(current_point[0], next_point[0]), max(current_point[0], next_point[0]) + 1):
                for y in range(min(current_point[1], next_point[1]), max(current_point[1], next_point[1]) + 1):
                    result.add((x,y))
            current_point = next_point
    return result

def run_sand(data):
    source = (500,0)
    still_sand = set([])

    result = []
    while source not in still_sand:
        sand = source
        can_move = True
        floor = max([x[1] for x in data])+2

        while can_move:
            can_move = False
            down = (sand[0], sand[1]+1)
            left = (sand[0]-1, sand[1]+1)
            right = (sand[0]+1, sand[1]+1)
            if sand[1] + 1 == floor:
                can_move = False
                if len(result) == 0:
                    result.append(len(still_sand))
            elif down not in still_sand and down not in data:
                sand = down
                can_move = True
            elif left not in still_sand and left not in data:
                sand = left
                can_move = True
            elif right not in still_sand and right not in data:
                sand = right
                can_move = True

        if sand == source:
            result.append(len(still_sand) + 1)
            return tuple(result)
        still_sand.add(sand)

    return (0,0)

def solve(data):
    """Solve the puzzle for the given input"""
    result = run_sand(data)

    # Part 1
    solution1 = result[0]

    # Part 2
    solution2 = result[1]

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
