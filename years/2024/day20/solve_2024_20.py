"""
Solution for day 20 of year 2024
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return tuple(line.strip())


def find_cheats(data, min_nanoseconds_saved, max_manhattan_distance = 2):
    start = None
    end = None

    path = set()
    height = len(data)
    width = len(data[0])


    for y in range(1, height -1):
        for x in range(1, width - 1):
            if data[y][x] == '#':
                continue
            elif data[y][x] == 'S':
                start = (x,y)
            elif data[y][x] == 'E':
                end = (x,y)
            path.add((x,y))

    distances_start = get_distances(path, start)
    distances_end = get_distances(path, end)

    return do_find_cheats(height, width, distances_start, distances_end, path, min_nanoseconds_saved, max_manhattan_distance)

def do_find_cheats(height, width, distances_start, distances_end, path, min_nanoseconds_saved, max_manhattan_distance):
    count = 0

    directions = ((0,1), (0,-1), (1,0), (-1,0))
    key = list(distances_start.keys())[0]

    original_distance = distances_start[key] + distances_end[key]

    for y in range(1, height -1):
        for x in range(1, width - 1):
            if (x, y) not in distances_start:
                continue

            queue = [((x, y), 0)]
            seen = set()

            while queue:
                pos, distance = queue.pop(0)

                distance += 1

                for direction in directions:
                    new_pos = (pos[0] + direction[0], pos[1] + direction[1])
                    if new_pos[0] < 1 or new_pos[0] >= width - 1 or new_pos[1] < 1 or new_pos[1] >= height - 1:
                        continue
                    if new_pos in seen:
                        continue
                    seen.add(new_pos)

                    if new_pos in distances_end:
                        if original_distance - (distances_start[(x, y)] + distances_end[new_pos] + distance)  >= min_nanoseconds_saved:
                            count += 1
                    if distance < max_manhattan_distance:
                        queue.append((new_pos, distance))

    return count


def get_distances(path, origin):
    distances = {origin: 0}
    directions = ((0,1), (0,-1), (1,0), (-1,0))
    queue = [(origin, 0)]
    seen = set([origin])

    while queue:
        pos, distance = queue.pop(0)
        for direction in directions:
            new_pos = (pos[0] + direction[0], pos[1] + direction[1])
            if new_pos in seen:
                continue
            seen.add(new_pos)
            if new_pos in path:
                distances[new_pos] = distance + 1
                queue.append((new_pos, distance + 1))
    
    return distances

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = find_cheats(data, 100)

    # Part 2
    solution2 = find_cheats(data, 100, 20)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
