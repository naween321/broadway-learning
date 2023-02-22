nums = [3, 4, 2, 2, 1, 3, 3, 3]
repeated = []
for i_index, i in enumerate(nums):
    for j_index, j in enumerate(nums):
        if j_index == i_index:
            continue
        if i == j and i not in repeated:
            repeated.append(i)
print(repeated)
