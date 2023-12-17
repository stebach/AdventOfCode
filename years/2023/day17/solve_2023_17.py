"""
Solution for day 17 of year 2023
"""

import os
from queue import PriorityQueue

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: line.strip(), inputdata.readlines()))


def find_min_heat_loss(data, min_movement=1, max_movement=3):
    queue = PriorityQueue()
    queue.put((int(data[0][1]),(1,0),(1,0),1))
    queue.put((int(data[1][0]),(0,1),(0,1),1))
    visited = set()
    directions = [(0,-1),(-1,0),(0,1),(1,0)]

    while not queue.empty():
        cost, pos, last_direction, repetitions = queue.get()
        if (pos, last_direction, repetitions) in visited:
            continue
        visited.add((pos, last_direction, repetitions))
        if pos == (len(data[0]) - 1, len(data) -1) and repetitions >= min_movement:
            return cost
        for direction in directions:
            if (-direction[0], -direction[1]) == last_direction:
                continue
            if direction == last_direction and repetitions == max_movement:
                continue
            if direction != last_direction and repetitions < min_movement:
                continue
            new_pos = (pos[0] + direction[0], pos[1] + direction[1])
            if (new_pos[0] < 0 or new_pos[1] < 0 or new_pos[1] >= len(data) or new_pos[0] >= len(data[0])):
                continue
            queue.put(( cost + int(data[new_pos[1]][new_pos[0]]), new_pos, direction, repetitions + 1 if direction == last_direction else 1))

def part1(data):
    """Solve part 1"""
    return find_min_heat_loss(data)

def part2(data):
    """Solve part 2"""
    return find_min_heat_loss(data, 4, 10)

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
