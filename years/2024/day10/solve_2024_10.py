"""
Solution for day 10 of year 2024
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return tuple([int(x) for x in list(line.strip())])

def get_trailheads(data, distinct_paths = False):
    result = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 0:
                current = 0
                queue = [(x, y)]
                while current < 9 and len(queue) > 0:
                    current += 1
                    next_queue = []
                    for pos in queue:
                        for direction in directions:
                            target = (pos[0] + direction[0], pos[1] + direction[1])
                            if target[0] in range(len(data[0])) and target[1] in range(len(data)):
                                if data[target[1]][target[0]] == current:
                                    next_queue.append(target)
                    queue = next_queue
                    if not distinct_paths:
                        queue = list(set(queue))
                if len(queue) > 0:
                    result.append(len(queue))
    return result

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = sum(get_trailheads(data))

    # Part 2
    solution2 = sum(get_trailheads(data, True))
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
