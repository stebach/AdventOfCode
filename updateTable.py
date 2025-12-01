import os
import regex
from datetime import date
from functools import reduce

input_file = 'README.md'
with open(os.path.dirname(__file__) + "/" + input_file, "r", encoding="utf-8") as inputdata:
    data = inputdata.read()

today = str(date.today())
month = int(today[5:7])
year = int(today[0:4])
if month < 12:
    year = year - 1

years = []
for y in range(2015, year + 1):
    count = 0
    if os.path.exists('./years/' + str(y)):
        for d in range(1, 26):
            if os.path.exists('./years/' + str(y) + '/day' + str(d).rjust(2,'0')):
                count = count + 2
    if y >= 2025:
        years = years + [[y, count, 24]]
    else:
        years = years + [[y, count, 50]]

years.reverse()
years += [['overall', sum(map(lambda x: x[1], years)), sum(map(lambda x: x[2], years))]]

maxlen = reduce(lambda x, y: [
        max(len(str(x[0])), len(str(y[0]))),
        max(len(str(x[1])), len(str(y[1]))),
        max(len(str(x[2])), len(str(y[2]))),
    ], years)

maxlen = [maxlen[0] + 3, maxlen[1] + maxlen[2] + 4, maxlen[1] + maxlen[2] + 45]

newTable = '| Year'.ljust(maxlen[0]) + '| Stars'.ljust(maxlen[1]) + '| Progress'.ljust(maxlen[2]) + '''|
''' + '|'.ljust(maxlen[0], '-') + '|'.ljust(maxlen[1], '-')  + '|'.ljust(maxlen[2], '-')  + '''|
'''
for year in years:
    newTable = newTable + ('| ' + str(year[0])).ljust(maxlen[0]) + ('| ' + str(year[1]) + '/' + str(year[2])).ljust(maxlen[1]) + ('| ![](https://mdtools.ste.li/progress/' + str(year[1]) + '/' + str(year[2]) +'.png)').ljust(maxlen[2]) + '''|
'''

with open(os.path.dirname(__file__) + "/" + input_file, 'w') as file:
    file.write(regex.sub(pattern=r'\| Year.*?overall.*?\.png\)[ ]\|\n', repl=newTable, string=data, flags=regex.DOTALL))
