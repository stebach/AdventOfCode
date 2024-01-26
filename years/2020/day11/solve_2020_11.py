"""
Solution for day 11 of year 2020
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    directions = ((-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1))
    result = {}
    for y, row in enumerate(lines):
        for x, col in enumerate(row):
            if col == 'L':
                adjacent1 = []
                adjacent2 = []
                for direction in directions:
                    next_in_direction = get_next_in_direction(lines, (x,y), direction)
                    if next_in_direction[0] == None:
                        continue
                    adjacent2.append(next_in_direction[0])
                    if next_in_direction[1] == 1:
                        adjacent1.append(next_in_direction[0])
                result[(x,y)] = (tuple(adjacent1), tuple(adjacent2))
    return result

def get_next_in_direction(data, pos, direction):
    distance = 0
    while True:
        pos = (pos[0] + direction[0], pos[1] + direction[1])
        distance += 1
        if pos[0] < 0 or pos[1] < 0 or pos[1] >= len(data) or pos[0] >= len(data[pos[1]]):
            return (None, None)
        if data[pos[1]][pos[0]] == 'L':
            return (pos, distance)

def number_after_stabilization(data, with_distance=False):
    last_state = ''
    buffer = dict([[x,0] for x in data])
    data_index = 1 if with_distance else 0
    occupied_seats = 5 if with_distance else 4
    while last_state != "".join([str(buffer[x]) for x in buffer]):
        last_state = "".join([str(buffer[x]) for x in buffer])
        new_buffer = dict([[x,0] for x in data])
        for point in data:
            if buffer[point] == 0 and sum([buffer[x] for x in data[point][data_index]]) == 0:
                new_buffer[point] = 1
            elif buffer[point] == 1 and sum([buffer[x] for x in data[point][data_index]]) >= occupied_seats:
                new_buffer[point] = 0
            else:
                new_buffer[point] = buffer[point]
        buffer = new_buffer
    return sum([buffer[x] for x in buffer])

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = number_after_stabilization(data)

    # Part 2
    solution2 = number_after_stabilization(data, True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

