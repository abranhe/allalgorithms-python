# -*- coding: UTF-8 -*-
#
# Cocktail Shaker Sort Algorithm
# The All ▲lgorithms library for python
#
# Contributed by: Martmists
# Github: @martmists
#


def cocktail_shaker_sort(data):
    upper = len(data) - 1
    lower = 0

    no_swap = False
    while upper - lower > 1 and not no_swap:
        no_swap = True
        for j in range(lower, upper):
            if data[j + 1] < data[j]:
                data[j + 1], data[j] = data[j], data[j + 1]
                no_swap = False
        upper = upper - 1

        for j in range(upper, lower, -1):
            if data[j - 1] > data[j]:
                data[j - 1], data[j] = data[j], data[j - 1]
                no_swap = False
        lower = lower + 1

    return data
