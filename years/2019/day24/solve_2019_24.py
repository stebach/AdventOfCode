"""
Solution for day 24 of year 2019
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return list(map(parse_line, inputdata.readlines()))
    
def run_minutes(pattern, minutes=0, until_first_double=False):
    doubles = set()
    if until_first_double:
        minutes = 100000
    for minute in range(minutes):
        new_pattern = [[0,0,0,0,0] for x in range(5)]
        for x in range(5):
            for y in range(5):
                adjacent_bugs = 0
                if x > 0 and pattern[y][x-1] == '#':
                    adjacent_bugs += 1
                if x < 4 and pattern[y][x+1] == '#':
                    adjacent_bugs += 1
                if y > 0 and pattern[y-1][x] == '#':
                    adjacent_bugs += 1
                if y < 4 and pattern[y+1][x] == '#':
                    adjacent_bugs += 1
                if pattern[y][x] == '#' and adjacent_bugs != 1:
                    new_pattern[y][x] = '.'
                elif pattern[y][x] == '.' and adjacent_bugs in [1,2]:
                    new_pattern[y][x] = '#'
                else:
                    new_pattern[y][x] = pattern[y][x]
        pattern = new_pattern
        if until_first_double:
            pattern_string = ''.join([''.join(x) for x in pattern])
            if pattern_string in doubles:
                return pattern
            else:
                doubles.add(pattern_string)
    return pattern

def biodiversity_rating(pattern):
    total = 0
    for y, row in enumerate(pattern):
        for x, col in enumerate(row):
            if col == '#':
                total += pow(2, y*5 + x)
    return total

def parse_line(line):
    line = line.strip()
    return [*line]

def run_minutes_multilayer(pattern, minutes):
    for minute in range(minutes):
        new_pattern = []
        pattern = [[['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.']]] + pattern + [[['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.']]]
        for z in range(len(pattern)):
            new_layer = [['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.']]
            for x in range(5):
                for y in range(5):
                    if x == 2 and y == 2:
                        continue

                    adjacent_bugs = 0
                    if y == 0:
                        if z > 0 and pattern[z-1][1][2] == '#':
                            adjacent_bugs += 1
                    elif y == 3 and x == 2:
                        # check inner
                        if z < len(pattern) - 1:
                            if pattern[z+1][4][0] == '#':
                                adjacent_bugs += 1
                            if pattern[z+1][4][1] == '#':
                                adjacent_bugs += 1
                            if pattern[z+1][4][2] == '#':
                                adjacent_bugs += 1
                            if pattern[z+1][4][3] == '#':
                                adjacent_bugs += 1
                            if pattern[z+1][4][4] == '#':
                                adjacent_bugs += 1
                    else:
                        if pattern[z][y-1][x] == '#':
                            adjacent_bugs += 1

                    if y == 4:
                        if z > 0 and pattern[z-1][3][2] == '#':
                            adjacent_bugs += 1
                    elif y == 1 and x == 2:
                        # check inner
                        if z < len(pattern) - 1:
                            if pattern[z+1][0][0] == '#':
                                adjacent_bugs += 1
                            if pattern[z+1][0][1] == '#':
                                adjacent_bugs += 1
                            if pattern[z+1][0][2] == '#':
                                adjacent_bugs += 1
                            if pattern[z+1][0][3] == '#':
                                adjacent_bugs += 1
                            if pattern[z+1][0][4] == '#':
                                adjacent_bugs += 1
                    else:
                        if pattern[z][y+1][x] == '#':
                            adjacent_bugs += 1

                    if x == 4:
                        if z > 0 and pattern[z-1][2][3] == '#':
                            adjacent_bugs += 1
                    elif y == 2 and x == 1:
                        # check inner
                        if z < len(pattern) - 1:
                            if pattern[z+1][0][0] == '#':
                                adjacent_bugs += 1
                            if pattern[z+1][1][0] == '#':
                                adjacent_bugs += 1
                            if pattern[z+1][2][0] == '#':
                                adjacent_bugs += 1
                            if pattern[z+1][3][0] == '#':
                                adjacent_bugs += 1
                            if pattern[z+1][4][0] == '#':
                                adjacent_bugs += 1
                    else:
                        if pattern[z][y][x+1] == '#':
                            adjacent_bugs += 1

                    if x == 0:
                        if z > 0 and pattern[z-1][2][1] == '#':
                            adjacent_bugs += 1
                    elif y == 2 and x == 3:
                        # check inner
                        if z < len(pattern) - 1:
                            if pattern[z+1][0][4] == '#':
                                adjacent_bugs += 1
                            if pattern[z+1][1][4] == '#':
                                adjacent_bugs += 1
                            if pattern[z+1][2][4] == '#':
                                adjacent_bugs += 1
                            if pattern[z+1][3][4] == '#':
                                adjacent_bugs += 1
                            if pattern[z+1][4][4] == '#':
                                adjacent_bugs += 1
                    else:
                        if pattern[z][y][x-1] == '#':
                            adjacent_bugs += 1

                    if pattern[z][y][x] == '#' and adjacent_bugs != 1:
                        new_layer[y][x] = '.'
                    elif pattern[z][y][x] == '.' and adjacent_bugs in [1,2]:
                        new_layer[y][x] = '#'
                    else:
                        new_layer[y][x] = pattern[z][y][x]
                    
            new_pattern.append(new_layer)
        while sum([sum([0 if y == '.' else 1 for y in x]) for x in new_pattern[0]]) == 0:
            new_pattern.pop(0)
        while sum([sum([0 if y == '.' else 1 for y in x]) for x in new_pattern[len(new_pattern)-1]]) == 0:
            new_pattern.pop()
        
        pattern = new_pattern
    return pattern
        

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = biodiversity_rating(run_minutes(data, until_first_double=True))

    # Part 2
    layers = run_minutes_multilayer([data], 200)
    solution2 = sum([sum([sum([1 for x in y if x == '#']) for y in z]) for z in layers])

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
