# -*- coding: UTF-8 -*-
#
# Jump search works for a sorted array.
# The All ▲lgorithms library for python
#
# Contributed by: pieromoto
# Github: @pieromoto
#
import math 
  
def jump_search( arr, query): 
    arr_len = len(arr)
    prev = 0
    step = int(math.sqrt(arr_len))

    for i in range(step-1, arr_len, step):
        if(arr[i] >= query):
            break
        prev = i

    for j in range(prev, arr_len):
        if(arr[j] == query):
            return j

    return None