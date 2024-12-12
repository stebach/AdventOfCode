"""
Solution for day 12 of year 2024
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return tuple(line.strip())

def calc_fencing_price(data, discounted = False):
    groups = {}
    areas = []
    current_area = 1

    for y, r in enumerate(data):
        areas.append([])
        for x, c in enumerate(r):
            matching_group = None
            if y == 0 and x == 0:
                areas[y].append(current_area)
                groups[current_area] = [(x, y)]
                continue
            if x > 0 and c == data[y][x-1]:
                matching_group = areas[y][x-1]
            if y > 0 and c == data[y-1][x]:
                if matching_group and data[y][x-1] == data[y-1][x] and matching_group != areas[y-1][x]:
                    other_matching_group = areas[y-1][x]
                    for coords in groups[other_matching_group]:
                        groups[matching_group].append(coords)
                        areas[coords[1]][coords[0]] = matching_group
                    del groups[other_matching_group]
                else:
                    matching_group = areas[y-1][x]
            if not matching_group:
                current_area += 1
                matching_group = current_area
                groups[matching_group] = []
            areas[y].append(matching_group)
            groups[matching_group].append((x, y))
    
    directions = [(0,1), (1,0), (0,-1), (-1,0)]

    price = 0
    if not discounted:
        for g in groups:
            all_coords = tuple(groups[g])
            circumfrence = 0
            for coord in all_coords:
                circumfrence += 4
                for direction in directions:
                    if (coord[0] + direction[0], coord[1] + direction[1]) in all_coords:
                        circumfrence -= 1
            price += circumfrence * len(all_coords)
    else:
        for g in groups:
            edges = set()
            all_coords = tuple(groups[g])
            for coord in all_coords:
                for direction in directions:
                    if (coord[0] + direction[0], coord[1] + direction[1]) not in all_coords:
                        edges.add(((coord[0] + direction[0] * 0.3, coord[1] + direction[1] * 0.3), (abs(direction[1]), abs(direction[0]))))

            sides = set()
            for edge in edges:
                if not ((edge[0][0] + edge[1][0], edge[0][1] + edge[1][1]), edge[1]) in edges:
                    sides.add(edge)

            price += len(sides) * len(all_coords)

    return price

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = calc_fencing_price(data)

    # Part 2
    solution2 = calc_fencing_price(data, True)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
