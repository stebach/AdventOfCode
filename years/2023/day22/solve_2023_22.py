"""
Solution for day 22 of year 2023
"""

import os
from queue import PriorityQueue

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    coords = [[int(y) for y in x.split(',')] for x in line.strip().split('~')]
    return (
        [
            min(coords[0][2], coords[1][2]),
            min(coords[0][1], coords[1][1]),
            min(coords[0][0], coords[1][0])
        ],
        [
            max(coords[0][2], coords[1][2]),
            max(coords[0][1], coords[1][1]),
            max(coords[0][0], coords[1][0])
        ]
    )

def get_movement(piece, data):
    if piece[0][0] == 1:
        return 0
    to_check = [x for x in data if x != piece and x[1][0] < piece[0][0]]

    distance_to_hit = piece[0][0] - 1

    for check in to_check:
        distance = piece[0][0] - check[1][0] - 1
        if distance < distance_to_hit:
            overlap_x = piece[0][2] <= check[1][2] and check[0][2] <= piece[1][2]
            overlap_y = piece[0][1] <= check[1][1] and check[0][1] <= piece[1][1]
            if overlap_x and overlap_y:
                distance_to_hit = distance

    return distance_to_hit

def get_above(piece, data):
    result = []
    to_check = [x for x in data if x != piece and x[0][0] == piece[1][0] +1]

    for check in to_check:
        overlap_x = piece[0][2] <= check[1][2] and check[0][2] <= piece[1][2]
        overlap_y = piece[0][1] <= check[1][1] and check[0][1] <= piece[1][1]
        if overlap_x and overlap_y:
            result.append(check)

    return result

def move_down(data):
    queue = PriorityQueue()
    for piece in data:
        queue.put(piece)
    
    while not queue.empty():
        piece = queue.get()
        move = get_movement(piece, data)

        piece[0][0] -= move
        piece[1][0] -= move

    for piece in data:
        queue.put(piece)

def check_supporting(data):
    queue = PriorityQueue()
    for piece in data:
        queue.put(piece)

    supporting = {}
    supported_by = {}
    while not queue.empty():
        piece = queue.get()
        above = get_above(piece, data)
        for a in above:
            if str(piece) not in supporting:
                supporting[str(piece)] = []
            supporting[str(piece)].append(a)

            if str(a) not in supported_by:
                supported_by[str(a)] = []
            supported_by[str(a)].append(piece)
    return (supporting, supported_by)

def part1(data):
    """Solve part 1"""
    move_down(data)
    supporting, supported_by = check_supporting(data)

    safe_to_disintegrated = 0
    for piece in data:
        if str(piece) not in supporting:
            safe_to_disintegrated += 1
        else:
            safe = True
            for check in supporting[str(piece)]:
                if len(supported_by[str(check)]) == 1:
                    safe = False
                    break
            if safe:
                safe_to_disintegrated += 1
 
    return safe_to_disintegrated

def part2(data):
    """Solve part 2"""
    move_down(data)
    supporting, supported_by = check_supporting(data)

    falling = 0
    for piece in data:
        to_check = [piece]
        checked = set()
        while len(to_check):
            check = to_check.pop()
            checked.add(str(check))
            if str(check) in supporting:
                for other in supporting[str(check)]:
                    supported = False
                    for other_support in supported_by[str(other)]:
                        if str(other_support) not in checked:
                            supported = True
                            break
                    if not supported:
                        falling += 1
                        to_check.append(other)

    return falling

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
