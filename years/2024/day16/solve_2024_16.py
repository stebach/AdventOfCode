"""
Solution for day 16 of year 2024
"""

import os
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = {
        'start': None,
        'end': None,
        'path': set()
    }

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == 'S':
                result['start'] = (x, y)
                result['path'].add((x, y))
            elif char == 'E':
                result['end'] = (x, y)
                result['path'].add((x, y))
            elif char == '.':
                result['path'].add((x, y))

    return result

def lowest_score(data):
    queue = [(data['start'], (1, 0), 0, set([data['start']]))]
    min_score = -1
    visited = {
        data['start']: 0
    }
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
    best_spots = set()


    while queue:
        current, direction, score, current_path = queue.pop(0)

        if current == data['end']:
            if min_score == -1 or score < min_score:
                min_score = score
                best_spots = deepcopy(current_path)
            elif score == min_score:
                best_spots.update(current_path)
        elif visited[current] < score - 1000:
            continue 

        for dx, dy in directions:
            if dx == -direction[0] and dy == -direction[1]:
                continue
            new = (current[0] + dx, current[1] + dy)
            new_score = score + 1
            if (dx, dy) != direction:
                new_score += 1000
            if new in data['path'] and (new not in visited or visited[new] >= new_score - 1000):
                new_path = deepcopy(current_path)
                new_path.add(new)
                queue.append((new, (dx, dy), new_score, new_path))
                if new not in visited:
                    visited[new] = new_score
                elif new_score < visited[new]:
                    visited[new] = new_score

    return (min_score, len(best_spots))

def solve(data):
    """Solve the puzzle for the given input"""
    solutions = lowest_score(data)

    # Part 1
    solution1 = solutions[0]

    # Part 2
    solution2 = solutions[1]
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

