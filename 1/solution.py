import csv

import numpy as np

measurements = []
with open('input.txt') as f:
    reader = csv.reader(f, delimiter=' ',)
    for row in reader:
        measurements.append(int(row[0]))

slided = np.lib.stride_tricks.sliding_window_view(measurements, 3)

summed = [np.sum(window) for window in slided]
differences = np.ediff1d(summed)

count = 0
for diff in differences:
    if diff > 0:
        count += 1

print(count)