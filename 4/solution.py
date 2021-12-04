import csv

import numpy as np

bingo_numbers = []
bingo_tables = []

with open('input.txt') as f:
    reader = csv.reader(f, delimiter='\n',)
    for idx, row in enumerate(reader):
        if idx == 0:
            number_sequence = row[0].split(',')
            for number in number_sequence:
                bingo_numbers.append(int(number))

        else:
            if not row:
                bingo_tables.append([])
            else:
                bingo_tables[-1].append([int(number) for number in row[0].split(' ') if number])

bingo_tables = np.asarray(bingo_tables)

def check_if_bingo(numbers):
    numbers = np.asarray(numbers)

    for i in range(0, 6):
        col_occurences = np.where(i == numbers[:, 0])
        row_occurences = np.where(i == numbers[:, 1])
        if len(row_occurences[0]) == 5:
            return True, list(row_occurences)
        if len(col_occurences[0]) == 5:
            return True, list(col_occurences)

    return False, []

occurences = []
for i in range(0, bingo_tables.shape[0]):
    occurences.append([])

hit_numbers = []
drafted = []
idx = 0

erased_indexes = []
try:
    for draft in bingo_numbers:
        drafted.append(draft)
        for idx, table in enumerate(bingo_tables):

            row, col = np.where(table == draft)

            if len(col) == 1 and len(row) == 1:
                occurences[idx].append([col[0], row[0]])
                bingo, occ = check_if_bingo(occurences[idx])
                if bingo:

                    # FOR PART 2
                    if bingo_tables.shape[0] - len(erased_indexes) > 1:
                        bingo_tables[idx] = np.zeros((5, 5))
                        erased_indexes.append(idx)

                    else:
                        # FOR PART 1
                            for hit_number in drafted:
                                # hit_number = bingo_numbers[hit_id]
                                table[np.where(hit_number == table)] = 0
                            answer = np.sum(table) * draft
                            print(answer)
                            quit()

except Exception as err:
    pass
    print(err)

