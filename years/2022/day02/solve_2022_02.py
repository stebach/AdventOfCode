"""
Solution for day 02 of year 2022
"""

import os

VALUES = {
    "A": { # rock
        "val": 1,
        "win": "C",
        "lose": "B"
    },
    "B": { # paper
        "val": 2,
        "win": "A",
        "lose": "C"
    },
    "C": { # scissors
        "val": 3,
        "win": "B",
        "lose": "A"
    }
}

def puzzle_input():
    """Parsed input"""
    with open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8") as inputdata:
        return tuple(map(process_line, inputdata.readlines()))

def process_line(line):
    """
    >>> process_line("A Y\n"])
    ("A","B")
    """
    temp = line.strip().split(" ")
    return (temp[0], chr(ord(temp[1])-23))

def score_game(game):
    """
    >>> score_game(("A","B"),("B","A"),("C","C"))
    15
    """
    return_value = VALUES[game[1]]["val"]
    if VALUES[game[1]]["win"] == game[0]:
        return_value += 6
    elif game[1] == game[0]:
        return_value += 3
    return return_value

def part1(data):
    """Solve part 1"""
    return sum(map(score_game, data))

def score_game2(game):
    """
    >>> score_game(("A","B"),("B","A"),("C","C"))
    12
    """
    if game[1] == "A": #lose
        return score_game((game[0], VALUES[game[0]]["win"]))
    elif game[1] == "B": #draw
        return score_game((game[0], game[0]))
    else: #win
        return score_game((game[0], VALUES[game[0]]["lose"]))

def part2(data):
    """Solve part 2"""
    return sum(map(score_game2, data))

def solve(data):
    """Solve the puzzle for the given input"""
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = puzzle_input()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
