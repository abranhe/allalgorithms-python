# -*- coding: UTF-8 -*-
#
# Stooge Sort Algorithm
# The All ▲lgorithms library for python
#
# Contributed by: Martmists
# Github: @martmists
#


def stooge_sort(seq, start=0, end=None):
    if end is None:
        end = len(seq) - 1
    if seq[start] > seq[end]:
        seq[start], seq[end] = seq[end], seq[start]
    if (end - start + 1) > 2:
        third = (end - start + 1) // 3
        stooge_sort(seq, start, end-third)
        stooge_sort(seq, start+third, end)
        stooge_sort(seq, start, end-third)
    return seq
