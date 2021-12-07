import csv

import numpy as np
from sklearn.metrics import mean_squared_error

# crab_positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

crab_positions = []
with open('input.txt') as f:
    reader = csv.reader(f, delimiter=',',)
    for row in reader:
        for number in row:
            crab_positions.append(int(number))


def calc_consumption(position, crab_positions):

    final_cost = 0
    for crab in crab_positions:
        diff = abs(position - crab)
        final_cost += np.sum(np.arange(1, diff + 1))

    return final_cost


fuel_consumption = []
cost_values = []
for idx, i in enumerate(range(0, max(crab_positions))):
    align_position = np.ones([1, len(crab_positions)]) * i

    fuel_consumption.append(mean_squared_error(align_position[0], crab_positions))
    costs = calc_consumption(i, crab_positions)
    cost_values.append(costs)

final_cost = min(cost_values)

print('Final cost: ', final_cost)
