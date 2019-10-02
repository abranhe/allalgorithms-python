# -*- coding: UTF-8 -*-
#
# Shell Sort Algorithm
# The All ▲lgorithms library for python
#
# Contributed by: Elias
# Github: @eliasbayona
#

def shell_sort(arr): 
    n = len(arr) 
    h = int(n/2)


    while h > 0: 
        for i in range(h,n):
            
            temp = arr[i] 
            j = i 

            while  j >= h and arr[j-h] >temp: 
                arr[j] = arr[j-h] 
                j -= h 

            arr[j] = temp 

        h = int(h/2)
        
    return arr

