"""
Solution for day 02 of year 2022
"""

import os

def process_line(line):
    """
    >>> process_line("A Y\n"])
    ("A","B")
    """
    temp = line.strip().split(" ")
    return (temp[0], chr(ord(temp[1])-23))

with open(os.path.dirname(__file__) + "/day02_input.txt", "r", encoding="utf-8") as inputdata:
    # as tuple
    data = tuple(map(process_line, inputdata.readlines()))

values = {
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

def score_game(game):
    """
    >>> score_game(("A","B"),("B","A"),("C","C"))
    15
    """
    return_value = values[game[1]]["val"]
    if values[game[1]]["win"] == game[0]:
        return_value += 6
    elif game[1] == game[0]:
        return_value += 3
    return return_value

def score_game2(game):
    """
    >>> score_game(("A","B"),("B","A"),("C","C"))
    12
    """
    if game[1] == "A": #lose
        return score_game((game[0], values[game[0]]["win"]))
    elif game[1] == "B": #draw
        return score_game((game[0], game[0]))
    else: #win
        return score_game((game[0], values[game[0]]["lose"]))

print(sum(map(score_game, data)))
print(sum(map(score_game2, data)))
