# -*- coding: UTF-8 -*-
#
# Bubble Sort Algorithm
# The All ▲lgorithms library for python
#
# Contributed by: Martmists
# Github: @martmists
#


def bubble_sort(seq):
    for i in range(len(seq)):
        for j in range(len(seq)-i-1):
            if seq[j] > seq[j+1]:
                # Swap if both are not in order
                seq[j], seq[j+1] = seq[j+1], seq[j]

    return seq
