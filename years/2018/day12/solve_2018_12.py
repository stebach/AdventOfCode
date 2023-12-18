"""
Solution for day 12 of year 2018
"""

import os
from collections import deque
import itertools

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    return tuple([lines[0][15:].strip(), {
        x[0:5]: x[9] for x in lines[2:] 
    }])

def count_for_steps(chars, dict, steps):
    pos = 0
    last_chars = ''
    last_pos = 0
    for step in range(steps):
        new_chars = ''
        chars = '....' + chars + '....'
        pos -= 2
        for x in range(len(chars) -5):
            key = chars[x:x+5]
            if key in dict:
                new_chars += dict[key]
            else:
                new_chars += '.'
        pos += new_chars.index('#')
        chars = new_chars.lstrip('.').rstrip('.')
        if last_chars == chars:
            pos += (pos - last_pos) * (steps - step - 1)
            break
        last_chars = chars
        last_pos = pos
    return sum([x[0]+pos for x in enumerate(chars) if x[1] == '#'])

def part1(data):
    """Solve part 1"""
    return count_for_steps(data[0], data[1], 20)

def part2(data):
    """Solve part 2"""
    return count_for_steps(data[0], data[1], 50_000_000_000)

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
