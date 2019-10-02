# -*- coding: UTF-8 -*-
#
# Quick Sort Algorithm
# The All ▲lgorithms library for python
#
# Contributed by: Brian D. Hopper
# Github: @bubbabeans
#
def partition(xs, start, end):
    follower = leader = start
    while leader < end:
        if xs[leader] <= xs[end]:
            xs[follower], xs[leader] = xs[leader], xs[follower]
            follower += 1
        leader += 1
    xs[follower], xs[end] = xs[end], xs[follower]
    return follower

def _quicksort(xs, start, end):
    if start >= end:
        return
    p = partition(xs, start, end)
    _quicksort(xs, start, p-1)
    _quicksort(xs, p+1, end)
    
def quicksort(xs):
    _quicksort(xs, 0, len(xs)-1)

# To use: create a list and send it to quicksort:  quicksort(list placed here)
