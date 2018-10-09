# -*- coding: UTF-8 -*-
#
# Insertion Sort Algorithm
# The All ▲lgorithms library for python
#
# Contributed by: Martmists
# Github: @martmists
#


def insertion_sort(arr):
	if len(arr) == 1:
		return arr

	for i in range(1, len(arr)):
		j = i - 1
		while j >= 0 and arr[j] > arr[i]:
			j -= 1
		arr.insert(j + 1, arr.pop(i))

	return arr
