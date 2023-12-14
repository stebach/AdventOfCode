"""
Solution for day 09 of year 2018
"""

import os
import regex
from collections import deque

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return parse_line(inputdata.read().strip())

def parse_line(line):
    match = regex.findall(r'^([0-9]+) players; last marble is worth ([0-9]+) points', line)
    return tuple(map(int, match[0]))

def parse_lines(lines):
    return [x for x in lines]

def part1(data):
    """Solve part 1"""
    queue = deque([0])
    players = [0] * data[0]
    currentPlayer = 0
    for x in range(1, data[1] + 1):
        if (x % 23 == 0):
            queue.appendleft(queue.pop())
            queue.appendleft(queue.pop())
            queue.appendleft(queue.pop())
            queue.appendleft(queue.pop())
            queue.appendleft(queue.pop())
            queue.appendleft(queue.pop())
            players[currentPlayer] += x + queue.pop()
        else:
            queue.append(queue.popleft())
            queue.append(queue.popleft())
            queue.appendleft(x)
        currentPlayer = (currentPlayer + 1) % data[0]
    return max(players)

def part2(data):
    """Solve part 2"""
    return part1((data[0], data[1] * 100))

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
