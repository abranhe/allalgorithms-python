# Stooge Sort

Stooge sort is a recursive sorting algorithm. It is notable for its exceptional bad time complexity of O(n^(log 3 / log 1.5)) = O(n^2.7095...). The running time of the algorithm is thus slower compared to reasonable sorting algorithms, and is slower than Bubble sort, a canonical example of a fairly inefficient sort. It is however more efficient than Slowsort.

## Install

```
pip install allalgorithms
```

## Usage

```py
from allalgorithms.sorting import stooge_sort

arr = [77, 2, 10, -2, 1, 7]

print(stooge_sort(arr))
# -> [-2, 1, 2, 7, 10, 77]
```

## API

### stooge_sort(array)

> Returns a sorted array

##### Params:

- `array`: Unsorted Array
