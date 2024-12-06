"""
Solution for day 06 of year 2024
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = {
        'w': 0,
        'h': 0,
        'guard': {
            'pos': (0,0),
            'direction': (0,0)
        },
        'obstacles': set()
    }

    directions = {
        '^': (0,-1),
        '>': (1,0),
        'v': (0,1),
        '<': (-1,0)
    }

    for y, line in enumerate(lines):
        result['h'] = y + 1
        for x, char in enumerate(line):
            result['w'] = x + 1
            if char == '#':
                result['obstacles'].add((x,y))
            if char in directions:
                result['guard'] = {
                    'pos': (x,y),
                    'direction': directions[char]
                }

    return result

def count_visited(data):
    return len(get_visited(data)) - 1

def get_visited(data):
    current_pos = data['guard']['pos']
    current_dir = data['guard']['direction']

    visited = set((current_pos,))

    while current_pos[0] >= 0 and current_pos[0] < data['w'] and current_pos[1] >= 0 and current_pos[1] < data['h']:
        while (current_pos[0] + current_dir[0], current_pos[1] + current_dir[1]) in data['obstacles']:
            current_dir = (-current_dir[1], current_dir[0])
        current_pos = (current_pos[0] + current_dir[0], current_pos[1] + current_dir[1])
        visited.add(current_pos)
    
    return visited

def find_loop_possibilities(data):
    visited = get_visited(data)
    if data['guard']['pos'] in visited:
        visited.remove(data['guard']['pos'])
    loop_count = 0
    obstacles = data['obstacles']
    for pos in visited:
        current_pos = data['guard']['pos']
        current_dir = data['guard']['direction']
        path = set()
        while current_pos[0] >= 0 and current_pos[0] < data['w'] and current_pos[1] >= 0 and current_pos[1] < data['h']:
            while (current_pos[0] + current_dir[0], current_pos[1] + current_dir[1]) in obstacles \
                or (current_pos[0] + current_dir[0], current_pos[1] + current_dir[1]) == pos:
                current_dir = (-current_dir[1], current_dir[0])
            current_pos = (current_pos[0] + current_dir[0], current_pos[1] + current_dir[1])

            if (current_pos, current_dir) in path:
                loop_count += 1
                break

            path.add((current_pos, current_dir))

    return loop_count

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = count_visited(data)

    # Part 2
    solution2 = find_loop_possibilities(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
