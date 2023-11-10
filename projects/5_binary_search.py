def binary_search(array, objective, lower_limit=None, upper_limt=None):
    if lower_limit is None:
        lower_limit = 0

    if upper_limt is None:
        upper_limt = len(array) - 1

    if upper_limt < lower_limit:
        return -1

    midpoint = (lower_limit + upper_limt) // 2

    if array[midpoint] == objective:
        return midpoint
    elif objective < array[midpoint]:
        return binary_search(array, objective, lower_limit, midpoint - 1)
    else:
        return binary_search(array, objective, midpoint + 1, upper_limt)


long_list = list(range(1, 10001, 3))
print(long_list)


print(binary_search(long_list, 7))
