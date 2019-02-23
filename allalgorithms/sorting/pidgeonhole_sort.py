# -*- coding: UTF-8 -*-
#
# Pigeonhole Sort Algorithm
# The All ▲lgorithms library for python
#
# Contributed by: Martmists
# Github: @martmists
#

def pidgeonhole_sort(data):
    minimum = min(data)
    size = max(data) - minimum + 1
    holes = [0] * size
    for item in data:
        holes[item - minimum] += 1
    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            data[i] = count + minimum
            i += 1
    return data
