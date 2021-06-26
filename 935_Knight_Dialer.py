def neighbors():
    d_neighbors = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4] }

    return d_neighbors

d_neighbors = neighbors()
distinct_numbers = [1] * 10   # n = 1

for _ in range(1, n):
    next_distinct_numbers = [0] * 10
    for from_num in range(10):
        for to_num in d_neighbors[from_num]:
            next_distinct_numbers[to_num] += distinct_numbers[from_num]

    distinct_numbers = next_distinct_numbers

return sum(distinct_numbers) % (10**9 + 7)
