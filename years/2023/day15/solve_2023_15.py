"""
Solution for day 15 of year 2023
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_line(inputdata.read())

def parse_line(line):
    return line.strip().split(',')

def parse_lines(lines):
    return list(map(split_line, lines))

def split_line(line):
    if line[-1:] == '-':
        return [line[:-1], '-']
    parts = line.split('=')
    return [parts[0], '=', int(parts[1])]

def hash(string):
    result = 0
    for char in ([*string]):
        result = (result + ord(char)) * 17 % 256
    return result

def part1(data):
    """Solve part 1"""
    return sum([hash(x) for x in data])

def find_pos(key, boxes):
    check = [x for x in boxes if x[0] ==key]
    if len(check) > 0:
        return boxes.index(check[0])
    return -1

def calc_focusing_power(box):
    if len(box[1]) == 0:
        return 0
    return sum([(1 + box[0]) * (x[0]+1) * x[1][1] for x in enumerate(box[1])])

def part2(data):
    """Solve part 2"""
    data = parse_lines(data)
    boxes = [[] for x in range(257)]
    for line in data:
        pos = hash(line[0])
        if line[1] == '-':
            pos2 = find_pos(line[0], boxes[pos])
            if pos2 > -1:
                del boxes[pos][pos2]
        if line[1] == '=':
            pos2 = find_pos(line[0], boxes[pos])
            if pos2 > -1:
                boxes[pos][pos2][1] = line[2]
            else:
                boxes[pos].append([line[0], line[2]])
    
    return sum(list(map(calc_focusing_power,  enumerate(boxes))))

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
