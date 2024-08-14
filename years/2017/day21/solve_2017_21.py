"""
Solution for day 21 of year 2017
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return dict(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip().split(' => ')
    return tuple([line[0], tuple(line[1].split('/'))])

def count_on(data, iterations, initial_grid = None):
    grid = [
        ['.','#','.'],
        ['.','.','#'],
        ['#','#','#'],
    ]

    if initial_grid:
        grid = initial_grid

    for i in range(iterations):

        partlen = 3
        if len(grid) % 2 == 0:
            partlen = 2
        
        if len(grid) == 9:
            result = 0
            for row in range(3):
                for col in range(3):
                    result += count_on(data, iterations - i, [x[col*3:col*3+3] for x in grid[row*3:row*3+3]])
            return result
        else:
            newsize = len(grid) // partlen * (partlen + 1)
            new_grid = [[0] * newsize for x in range(newsize)]

            for row in range(len(grid) // partlen):
                for col in range(len(grid) // partlen):
                    key = '/'.join([''.join(x[col*partlen:col*partlen+partlen]) for x in grid[row*partlen:row*partlen+partlen]])
                    max = 100
                    while key not in data:
                        key2 = '/'.join([x[::-1] for x in key.split('/')])
                        if key2 not in data:
                            key = iteratekey(key)
                        else:
                            key = key2
                        max -= 1
                        if max < 1:
                            print("xxx")
                            exit()
                    for row2 in range(partlen + 1):
                        for col2 in range(partlen + 1):
                            new_grid[row * (partlen + 1) + row2][col * (partlen + 1) + col2] = data[key][row2][col2]

            grid = new_grid

    return sum([x.count('#') for x in grid])

def iteratekey(key):
    if len(key) == 5:
        key = key[1]  + key[4] + "/" + key[0]  + key[3]
    elif len(key) == 11:
        key = key[2] + key[6] + key[10] + "/" + key[1] + key[5] + key[9] + "/" + key[0] + key[4] + key[8]
    else:
        print(key)
        print("UNKNOWN LEN: " + str(len(key)))
        exit()
    return key

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = count_on(data, 5)

    # Part 2
    solution2 = count_on(data, 18)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

