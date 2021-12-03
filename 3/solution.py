import csv

import numpy as np

diagnostics = []
with open('input.txt') as f:
    reader = csv.reader(f, delimiter='\n',)
    for row in reader:
        diagnostics.append([int(digit) for digit in row[0]])

diagnostics = np.asarray(diagnostics)

# 1 Part

# gamma_binary = []
# epsilon_binary = []
# for i in range(0, diagnostics.shape[1]):
#     col = diagnostics[:, i]
#     unique, counts = np.unique(col, return_counts=True)
#     gamma_binary.append(unique[np.argmax(counts)])
#     epsilon_binary.append(unique[np.argmin(counts)])
#
# gamma_rate = 0
# for idx, digit in enumerate(reversed(gamma_binary)):
#     if digit:
#         gamma_rate += 2**idx
#
# epsilon_rate = 0
# for idx, digit in enumerate(reversed(epsilon_binary)):
#     if digit:
#         epsilon_rate += 2 ** idx
#
# answer = gamma_rate * epsilon_rate
#
# print(answer)

# 2 Part

# O2 Rating
filtered_bits = []
o2_rating = diagnostics.copy()
for bit_id in range(0, o2_rating.size):

    if o2_rating.shape[0] == 1:
        break

    col = o2_rating[:, bit_id]
    unique, counts = np.unique(col, return_counts=True)
    if len(np.unique(counts)) == 1:
        most_common_bit = 1
    else:
        most_common_bit = unique[np.argmax(counts)]

    qualified_ids = np.where(o2_rating[:, bit_id] == most_common_bit)

    for id in qualified_ids:
        filtered_bits.append(o2_rating[id])

    o2_rating = np.asarray(filtered_bits[0])
    filtered_bits = []

o2_rate = 0
for idx, bit in enumerate(reversed(o2_rating[0])):
    if bit:
        o2_rate += 2 ** idx

print(o2_rate)

filtered_bits = []
co2_rating = diagnostics.copy()

for bit_id in range(0, co2_rating.size):

    if co2_rating.shape[0] == 1:
        break

    col = co2_rating[:, bit_id]
    unique, counts = np.unique(col, return_counts=True)
    if len(np.unique(counts)) == 1:
        most_common_bit = 1
    else:
        most_common_bit = unique[np.argmax(counts)]

    qualified_ids = np.where(co2_rating[:, bit_id] != most_common_bit)
    for id in qualified_ids:
        filtered_bits.append(co2_rating[id])

    co2_rating = np.asarray(filtered_bits[0])
    filtered_bits = []

co2_rate = 0
for idx, bit in enumerate(reversed(co2_rating[0])):
    if bit:
        co2_rate += 2 ** idx

print(co2_rate)

print('Answer: ', co2_rate * o2_rate)
