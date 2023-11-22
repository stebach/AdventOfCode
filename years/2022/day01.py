"""
Solution for day 01 of year 2022
"""

import os

with open(os.path.dirname(__file__) + "/day01_input.txt", "r", encoding="utf-8") as inputdata:
    data = inputdata.read()

data = data.split("\n\n")
data = [tuple(map(int, row.split("\n"))) for row in data]
data.sort(key=sum, reverse=True)

print(sum(data[0]))
print(sum(map(sum, data[0:3])))
