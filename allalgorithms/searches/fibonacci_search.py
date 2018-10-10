# -*- coding: UTF-8 -*-
#
# Fibonacci search works for a sorted array.
# The All ▲lgorithms library for python
#
# Contributed by: dieterpl
# Github: @dieterpl
#
def fibonacci_search(arr, query):
    fib2, fib1 = 0, 1
    fib = fib2 + fib1
    hi = len(arr) - 1
    while fib <= hi:
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1
    offset = -1
    while fib > 1:
        i = min(offset + fib2, hi)
        if arr[i] < query:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif arr[i] > query:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i
    if fib1 and arr[offset + 1] == query:
        return offset + 1
    return None
