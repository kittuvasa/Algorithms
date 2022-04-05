def bin_packing_next_fit(arr, capacity):
    c = capacity
    bin_capacity = c
    bin_used = 1
    for element in arr:
        if element <= bin_capacity:
            bin_capacity -= element
        else:
            bin_used += 1
            bin_capacity = c - element
    print(bin_used, "bins can be used next fit")


def bin_packing_first_fit(arr, capacity):
    c = capacity
    bin_used = 0
    bins = [0]*len(arr)

    for element in arr:
        j = 0
        while j < bin_used:
            if element <= bins[j]:
                bins[j] -= element
                break
            j += 1
        if j == bin_used:
            bins[j] = c - element
            bin_used += 1
    print(bin_used, "bins can be used first fit")


def bin_packing_best_fit(arr, capacity):
    c = capacity
    bin_used = 0
    bins = []
    for element in arr:
        loc, minimum = -5, 10000000000
        for index, i in enumerate(bins):
            if i >= element and i != 0:
                diff = i - element
                if diff <= minimum:
                    loc = index
                    minimum = diff
        if loc == -5:
            bin_used += 1
            bins.append(c - element)
        else:
            bins[loc] = bins[loc] - element
    print(bin_used, "bins can be used best fit")


bin_packing_next_fit([2, 5, 4, 7, 1, 3, 8], 10)
bin_packing_first_fit([2, 5, 4, 7, 1, 3, 8], 10)
bin_packing_best_fit([2, 5, 4, 7, 1, 3, 8], 10)
