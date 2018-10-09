# -*- coding: UTF-8 -*-
#
# Bubble Sort Algorithm
# The All ▲lgorithms library for python
#
# Contributed by: Martmists
# Github: @martmists
#


def selection_sort(seq):
    for i in range(len(seq)):
        min_idx = i
        for j in range(min_idx, len(seq)):
            if seq[j] < seq[min_idx]:
                min_idx = j

        seq[i], seq[min_idx] = seq[min_idx], seq[i]
    return seq
