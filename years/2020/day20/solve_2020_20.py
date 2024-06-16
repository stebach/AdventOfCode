"""
Solution for day 20 of year 2020
"""

import os
import numpy as np
from copy import deepcopy

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())



def parse_lines(lines):
    result = []
    currentTile = {}
    for line in lines:
        line = line.strip()
        if line[0:4] == 'Tile':
            currentTile = {
                "id": int(line[5:-1]),
                "lines": [],
                "matches":[]
            }
            result.append(currentTile)
        elif len(line) > 0:
            currentTile['lines'].append(line)
    return [addSides(x) for x in result]

def addSides(tile):
    tile["top"] = tile["lines"][0]
    tile["bottom"] = tile["lines"][-1][::-1]
    tile["left"] = ("".join([x[0] for x in tile["lines"]]))[::-1]
    tile["right"] = "".join([x[-1] for x in tile["lines"]])
    return tile

def arrange(data):
    directions = ['top','bottom','left','right']
    for x in range(len(data)-1):
        for y in range(x + 1, len(data)):
            doBreak = False
            for xline in directions:
                for yline in directions:
                    if data[x][xline] == data[y][yline] or data[x][xline] == data[y][yline][::-1]:
                        doBreak = True
                        data[x]['matches'].append([y, yline, xline, data[y]['id']])
                        data[y]['matches'].append([x, xline, yline, data[x]['id']])
                    if doBreak:
                        break
                if doBreak:
                    break

def get_corner_product(data):
    return np.prod([x['id'] for x in data if len(x['matches']) == 2])

def draw_map(data):
    arrange(data)
    grid = [[]]
    first = [x for x in data if len(x['matches']) == 2][0]
    while not ([x[2] for x in first['matches']] in [['bottom','right'],['right','bottom']]):
        rotate(first)
    pos_x = 0
    pos_y = 0
    grid[pos_y].append(first)

    finished = False
    while not finished:
        to_right = [x for x in grid[pos_y][pos_x]['matches'] if x[2] == 'right']
        if len(to_right) == 1:
            to_right_tile = data[to_right[0][0]]
            if to_right[0][1] == "top":
                rotate(to_right_tile)
                rotate(to_right_tile)
                rotate(to_right_tile)
            if to_right[0][1] == "right":
                rotate(to_right_tile)
                rotate(to_right_tile)
            if to_right[0][1] == "bottom":
                rotate(to_right_tile)
            current = "".join([x[-1] for x in grid[pos_y][pos_x]['lines']])
            next = "".join([x[0] for x in to_right_tile['lines']])
            if current != next:
                flip_horizontal(to_right_tile)
                next = "".join([x[0] for x in to_right_tile['lines']])
                if current != next:
                    print("ERR 1")
                    exit()
            grid[pos_y].append(to_right_tile)
            pos_x += 1
        else:
            pos_x = 0
            to_bottom = [x for x in grid[pos_y][pos_x]['matches'] if x[2] == 'bottom']
            if len(to_bottom) == 1:
                to_bottom_tile = data[to_bottom[0][0]]
                if to_bottom[0][1] == "right":
                    rotate(to_bottom_tile)
                    rotate(to_bottom_tile)
                    rotate(to_bottom_tile)
                if to_bottom[0][1] == "bottom":
                    rotate(to_bottom_tile)
                    rotate(to_bottom_tile)
                if to_bottom[0][1] == "left":
                    rotate(to_bottom_tile)
                current = grid[pos_y][pos_x]['lines'][-1]
                next = to_bottom_tile['lines'][0]
                if current != next:
                    flip_vertical(to_bottom_tile)
                    next = to_bottom_tile['lines'][0]
                    if current != next:
                        print("ERR 3")
                        exit()
                grid.append([])
                grid[pos_y + 1].append(to_bottom_tile)
                pos_y += 1
            else:
                finished = True
    
    map = []

    for row in grid:
        for line in range(1, len(row[0]['lines']) -1):
            mapline = []
            for col in range(len(row)):
                mapline.append(row[col]['lines'][line][1:-1])
            map.append("".join(mapline))
    return map

def flip_vertical(tile):
    tile['lines'] = [x[::-1] for x in tile['lines']]
    for x in tile['matches']:
        if x[2] == 'right':
            x[2] = 'left'
        elif x[2] == 'left':
            x[2] = 'right'

def flip_horizontal(tile):
    tile['lines'] = tile['lines'][::-1]
    for x in tile['matches']:
        if x[2] == 'top':
            x[2] = 'bottom'
        elif x[2] == 'bottom':
            x[2] = 'top'

def rotate(tile):
    tile['lines'] = ["".join([x[y] for x in tile['lines']])[::-1] for y in range(len(tile['lines']))]
    for x in tile['matches']:
        if x[2] == 'top':
            x[2] = 'right'
        elif x[2] == 'right':
            x[2] = 'bottom'
        elif x[2] == 'bottom':
            x[2] = 'left'
        elif x[2] == 'left':
            x[2] = 'top'

def get_roughness(data):
    monster = [
        (18,0),(0,1),(5,1),(6,1),(11,1),(12,1),(17,1),(18,1),(19,1),(1,2),(4,2),(7,2),(10,2),(13,2),(16,2)
    ]
    monster_width = 20
    monster_height = 3

    map = draw_map(data)

    monster_count = 0

    map = rotate_map(map)
    map = flip_map(map)

    rotations = 0
    while monster_count == 0 and rotations < 8:
        for y in range(len(map) - monster_height + 1):
            for x in range(len(map[0]) - monster_width + 1):
                found = True
                for pos in monster:
                    if map[y + pos[1]][x + pos[0]] != '#':
                        found = False
                        break
                if found:
                    monster_count += 1
        if monster_count == 0:
            map = rotate_map(map)
            rotations += 1
            if rotations == 4:
                map = flip_map(map)

    return sum([len([y for y in [*x] if y == '#']) for x in map]) - monster_count * len(monster)

def rotate_map(map):
    return ["".join([x[y] for x in map])[::-1] for y in range(len(map))]

def flip_map(map):
    return map[::-1]

def draw_monster(map, monster, x, y):
    for pos in monster:
        line = [*map[y+pos[1]]]
        line[x+pos[0]] = 'X'

        map[y+pos[1]] = ''.join(line)
    print(map)

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    data2 = deepcopy(data)
    arrange(data)
    solution1 = get_corner_product(data)

    # Part 2
    solution2 = get_roughness(data2)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
