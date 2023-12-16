"""
Solution for day 16 of year 2023
"""

import os
from functools import reduce

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(lambda line: line.strip(), inputdata.readlines()))

def count_energized(contraption, entry):
    energized = []
    beams = [entry]

    while len(beams) > 0:
        next_beams = []
        for beam in beams:
            moved_beam_pos = (beam[0][0] + beam[1][0], beam[0][1] + beam[1][1])
            moved_beam_directions = [beam[1]]
            if moved_beam_pos[0] < 0 or moved_beam_pos[0] >= len(contraption[0]) or moved_beam_pos[1] < 0 or moved_beam_pos[1] >= len(contraption):
                continue
            if contraption[moved_beam_pos[1]][moved_beam_pos[0]] == '/':
                if moved_beam_directions[0] == (0,1):
                    moved_beam_directions = [(-1,0)]
                elif moved_beam_directions[0] == (0,-1):
                    moved_beam_directions = [(1,0)]
                elif moved_beam_directions[0] == (1,0):
                    moved_beam_directions = [(0,-1)]
                elif moved_beam_directions[0] == (-1,0):
                    moved_beam_directions = [(0,1)]
            elif contraption[moved_beam_pos[1]][moved_beam_pos[0]] == '\\':
                if moved_beam_directions[0] == (0,1):
                    moved_beam_directions = [(1,0)]
                elif moved_beam_directions[0] == (0,-1):
                    moved_beam_directions = [(-1,0)]
                elif moved_beam_directions[0] == (1,0):
                    moved_beam_directions = [(0,1)]
                elif moved_beam_directions[0] == (-1,0):
                    moved_beam_directions = [(0,-1)]
            elif contraption[moved_beam_pos[1]][moved_beam_pos[0]] == '|':
                if moved_beam_directions[0] in ((1,0),(-1,0)):
                    moved_beam_directions = [(0,1),(0,-1)]
            elif contraption[moved_beam_pos[1]][moved_beam_pos[0]] == '-':
                if moved_beam_directions[0] in ((0,1),(0,-1)):
                    moved_beam_directions = [(1,0),(-1,0)]
            for moved_beam_direction in moved_beam_directions:
                moved_beam = (moved_beam_pos, moved_beam_direction)
                if not moved_beam in energized:
                    energized.append(moved_beam)
                    next_beams.append(moved_beam)
        beams = next_beams

    return len(reduce(lambda new_list, y: new_list + [y] if y not in new_list else new_list, [x[0] for x in energized], []))

def part1(data):
    """Solve part 1"""
    return count_energized(data,((-1,0),(1,0)))

def part2(data):
    """Solve part 2"""
    results = []
    to_check = [];
    to_check += [((x,-1),(0,1)) for x in range(0,len(data[0]))]
    to_check += [((x,len(data)),(0,-1)) for x in range(0,len(data[0]))]
    to_check += [((-1,x),(1,0)) for x in range(0,len(data))]
    to_check += [((len(data[0]),x),(-1,0)) for x in range(0,len(data[0]))]
    for check in to_check:
        result = count_energized(data, check)
        results += [result]
    return max(results)

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
