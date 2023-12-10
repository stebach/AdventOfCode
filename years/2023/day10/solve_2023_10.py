"""
Solution for day 10 of year 2023
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: line.strip(), inputdata.readlines()))

def solve_loop(data):
    row = [k for k,v in enumerate(data) if 'S' in v][0]
    col = data[row].index('S')

    visited = [[row, col]]

    connections = {
        'n': {
            'x': 0,
            'y': -1,
            '|':'n',
            'F':'e',
            '7':'w'
        },
        'e': {
            'x': 1,
            'y': 0,
            '-':'e',
            'J':'n',
            '7':'s'
        },
        's': {
            'x': 0,
            'y': 1,
            '|':'s',
            'J':'w',
            'L':'e'
        },
        'w': {
            'x': -1,
            'y': 0,
            '-':'w',
            'F':'s',
            'L':'n'
        }
    }

    pipes = []
    for connection in connections.items():
        checkX = col + connection[1]['x']
        checkY = row + connection[1]['y']
        if checkY > -1 and checkY < len(data) and checkX > -1 and checkX < len(data[checkY]) and data[checkY][checkX] in data[checkY][checkX] in connection[1]:
            pipes = pipes + [[checkY, checkX, connection[0]]]
            visited = visited + [[checkY, checkX]]
    
    distance = 1

    while pipes[0][0:2] != pipes[1][0:2]:
        new_pipes = []
        for pipe in pipes:
            next_direction = connections[pipe[2]][data[pipe[0]][pipe[1]]]
            new_pipes = new_pipes + [[pipe[0] + connections[next_direction]['y'], pipe[1] + connections[next_direction]['x'], next_direction]]
            visited = visited + [[pipe[0] + connections[next_direction]['y'], pipe[1] + connections[next_direction]['x']]]
        pipes = new_pipes
        distance = distance + 1

    return distance, visited


def part1(data):
    """Solve part 1"""
    distance, visited = solve_loop(data)
    return distance

def flood(to_flood, data):
    checked = []
    directions = [[-1,0],[0,-1],[1,0],[0,1]]
    while len(to_flood):
        new_flood = []
        for f in to_flood:
            checked = checked + [f]
            if data[f[0]][f[1]] in ". ":
                data[f[0]] = data[f[0]][:f[1]] + " " + data[f[0]][f[1]+1:]
                for d in directions:
                    new_check = [f[0] + d[0], f[1] + d[1]]
                    if new_check[0] > -1 and new_check[1] > -1 and new_check[0] < len(data) and new_check[1] < len(data[0]) and not new_check in checked and new_check not in new_flood and new_check not in to_flood:
                        new_flood = new_flood + [[f[0] + d[0], f[1] + d[1]]]
        to_flood = new_flood
    return data

def part2(data):
    """Solve part 2"""
    distance, visited = solve_loop(data)
    data2 = ["." * len(x) for x in data]
    for point in visited:
        data2[point[0]] = data2[point[0]][:point[1]] + data[point[0]][point[1]] + data2[point[0]][point[1]+1:]
    data3 = [[" " for x in range(len(data2[0]) * 2 + 1)] for y in range(len(data2) * 2 + 1)]

    for row in range(len(data2)):
        for col in range(len(data2[0])):
            if data2[row][col] == '-':
                data3[row*2][col*2] = '-'
                data3[row*2][col*2 - 1] = '-'
                data3[row*2][col*2 + 1] = '-'
            elif data2[row][col] == '|':
                data3[row*2][col*2] = '|'
                data3[row*2 + 1][col*2] = '|'
                data3[row*2 - 1][col*2] = '|'
            elif data2[row][col] == 'J':
                data3[row*2][col*2] = 'J'
                data3[row*2 - 1][col*2] = '|'
                data3[row*2][col*2 - 1] = '-'
            elif data2[row][col] == '7':
                data3[row*2][col*2] = '7'
                data3[row*2 + 1][col*2] = '|'
                data3[row*2][col*2 - 1] = '-'
            elif data2[row][col] == 'F':
                data3[row*2][col*2] = 'F'
                data3[row*2 + 1][col*2] = '|'
                data3[row*2][col*2 + 1] = '-'
            elif data2[row][col] == 'L':
                data3[row*2][col*2] = 'L'
                data3[row*2 - 1][col*2] = '|'
                data3[row*2][col*2 + 1] = '-'
            elif data2[row][col] in "S. ":
                data3[row * 2][col * 2] = data2[row][col]

    data3 = flood([[0,0], [len(data3) -1, len(data3[0]) -1]], ["".join(x) for x in data3])
    return ("\n".join(data3).count('.'))


def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
