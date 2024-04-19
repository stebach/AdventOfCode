"""
Solution for day 10 of year 2022
"""

import os

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(parse_line, inputdata.readlines()))

def parse_line(line):
    line = line.strip()
    if line == 'noop':
        return (1,)
    return (2, int(line.split(' ')[1]))

def get_cycles(data):
    result = []
    val = 1
    queue = [0]
    for line in data:
        while len(queue) > 0:
            result.append(val)
            val += queue.pop(0)
        queue.append(0)
        if line[0] == 2:
            queue.append(line[1])
    while len(queue) > 0:
        result.append(val)
        val += queue.pop(0)

    return result

def signal_strength(data):
    cycles = get_cycles(data)

    return sum([x*cycles[x] for x in [20,60,100,140,180,220]])

def draw(data):
    cycles = get_cycles(data)
    result = ""
    for i in range(240):
        if i > 0 and i % 40 == 0:
            result += "\n"
        if i%40 in [cycles[i+1]-1, cycles[i+1], cycles[i+1]+1]:
            result += '█'
        else:
            result += ' '

    return result

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = signal_strength(data)

    # Part 2
    solution2 = draw(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
