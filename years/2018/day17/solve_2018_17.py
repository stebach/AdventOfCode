"""
Solution for day 17 of year 2018
"""

import os
from collections import deque

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())
def parse_lines(lines):
    clay = []
    for line in lines:
        line = line.strip().split(', ')
        if line[0][0] == 'x':
            x = int(line[0][2:])
            y_range = [int(x) for x in line[1][2:].split('..')]
            for y in range(y_range[0], y_range[1]+1):
                if (x,y) not in clay:
                    clay.append((x,y))
        else:
            y = int(line[0][2:])
            x_range = [int(x) for x in line[1][2:].split('..')]
            for x in range(x_range[0], x_range[1]+1):
                if (x,y) not in clay:
                    clay.append((x,y))
    return tuple(clay)

def get_water_data(clay):
    to_check = deque()
    to_check.append((500,1))
    water_flowing = set()
    water_still = set()
    max_y = max([x[1] for x in clay])
    min_y = min([x[1] for x in clay])

    while len(to_check) > 0:
        check = to_check.popleft()
        below = (check[0],check[1] + 1)
        if below in clay or below in water_still:
            has_left_wall = False
            has_right_wall = False
            horizontal_check = [check]

            left = check[0] - 1
            while (left, check[1]) not in clay and ((left, below[1]) in clay or (left, below[1]) in water_still):
                horizontal_check.append((left, check[1]))
                left -= 1;
            if (left, check[1]) in clay:
                has_left_wall = True
            
            right = check[0] + 1
            while (right, check[1]) not in clay and ((right, below[1]) in clay or (right, below[1]) in water_still):
                horizontal_check.append((right, check[1]))
                right += 1;
            if (right, check[1]) in clay:
                has_right_wall = True

            if has_right_wall and has_left_wall:
                for coord in horizontal_check:
                    water_still.add(coord)
                water_still.add(check)
                if (check[0], check[1]-1) not in to_check:
                    to_check.append((check[0], check[1]-1))
            else:
                for coord in horizontal_check:
                    water_flowing.add(coord)
                if not has_left_wall:
                    if (left, check[1]) not in to_check:
                        to_check.append((left, check[1]))
                if not has_right_wall:
                    if (right, check[1]) not in to_check:
                        to_check.append((right, check[1]))
        else:
            if check[1] >= min_y:
                water_flowing.add(check)
            if below[1] <= max_y and below not in to_check:
                to_check.append(below)
    for x in water_still:
        if x in water_flowing:
            water_flowing.remove(x)
    return (len(water_still), len(water_flowing))

def part1(data):
    """Solve part 1"""
    result = get_water_data(data)
    return sum(result)

def part2(data):
    """Solve part 2"""
    result = get_water_data(data)
    return result[0]

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
