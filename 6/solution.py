import csv

import numpy as np

fishes_orig = []
with open('input.txt') as f:
    reader = csv.reader(f, delimiter='\n',)

    for row in reader:
        fishes_orig.append([int(time) for time in row[0].split(',')])

    # for row in reader:
    #     times = row[0].split(':')[-1]
    #     fishes_orig.append([int(time) for time in times.split(',')])

def update(fishes):

    zeros = np.where(fishes == 0)
    fishes[zeros] = 7 # +1
    fishes -= 1
    new_fishes = np.ones([1, len(zeros[0])]) * 8
    fishes_arr = np.append(fishes, new_fishes)

    return fishes_arr


def count(fishes):
    fish_dict = {}
    for i in range(0, 9):
        fish_dict[i] = len(np.where(fishes == i)[0])
    return fish_dict


def update_dict(fish_dict):
    prev_0 = fish_dict[0]

    for i in range(0, 9):
        if i == 6:
            fish_dict[i] = fish_dict[i + 1] + prev_0

        elif i == 8:
            fish_dict[i] = prev_0

        else:
            fish_dict[i] = fish_dict[i + 1]

    return fish_dict


fishes = np.asarray(fishes_orig[0].copy())
fish_dict = count(fishes)
for i in range(1, 257):
    fish_dict = update_dict(fish_dict)
    sum = 0
    for value in fish_dict.values():
        sum += value

    print(f'Day {i}', sum)

