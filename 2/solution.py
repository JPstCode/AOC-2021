import csv

# import pandas as pd
import numpy as np

movements = []
with open('input.txt') as f:
    reader = csv.reader(f, delimiter='\n',)
    for row in reader:
        movements.append([row[0].split(' ')[0], int(row[0].split(' ')[1])])

# 1)

# hor, depth
# position = [0, 0]

# for move in movements:
#     direction = move[0]
#     step = move[1]
#
#     if direction == 'up':
#         position[1] -= step
#
#     elif direction == 'down':
#         position[1] += step
#
#     else:
#          position[0] += step
#
# answer = position[0] * position[1]

# 2)

# hor, depth, aim
position = [0, 0, 0]

for move in movements:
    direction = move[0]
    step = move[1]

    if direction == 'up':
        position[2] -= step

    elif direction == 'down':
        position[2] += step
    else:
        position[0] += step
        position[1] += position[2] * step

answer = position[0] * position[1]
print(answer)