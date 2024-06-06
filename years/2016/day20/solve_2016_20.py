"""
Solution for day 20 of year 2016
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    return tuple([int(x) for x in line.strip().split('-')])

def get_lowest(data):
    lowest = 0

    check = [x for x in data if x[0] <= lowest and x[1] >= lowest]
    while len(check) > 0:
        lowest = check[0][1] + 1
        check = [x for x in data if x[0] <= lowest and x[1] >= lowest]
    return lowest

def count_allowed(data, last = 4294967295):
    blocked = []
    for row in data:
        check = [x for x in blocked if x[0] <= row[1] and x[1] >= row[0]]
        while len(check) > 0:
            tmp = check[0]
            if row[0] >= tmp[0] and row[1] <= tmp[1]:
                row = None
                break
            elif row[1] <= tmp[1]:
                row = (row[0], tmp[0] -1)
            elif row[0] >= tmp[0]:
                row = (tmp[1] + 1, row[1])
            elif row[0] <= tmp[0] and row[1] >= tmp[1]:
                blocked.remove(tmp)
            else:
                print('AHA!')
                print(check)
                print(row)
                exit()
            check = [x for x in blocked if x[0] <= row[1] and x[1] >= row[0]]
        if row is not None:
            blocked.append(row)
    
    return last - sum([x[1] - x[0] + 1 for x in blocked]) + 1

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_lowest(data)

    # Part 2
    solution2 = count_allowed(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

