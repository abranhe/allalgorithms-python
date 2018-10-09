# Selection Sort

In computer science, selection sort is a sorting algorithm, specifically an in-place comparison sort. It has O(n^2) time complexity, making it inefficient on large lists, and generally performs worse than the similar insertion sort. Selection sort is noted for its simplicity, and it has performance advantages over more complicated algorithms in certain situations, particularly where auxiliary memory is limited.

## Install

```
pip install allalgorithms
```

## Usage

```py
from allalgorithms.sorting import selection_sort

arr = [77, 2, 10, -2, 1, 7]

print(selection_sort(arr))
# -> [-2, 1, 2, 7, 10, 77]
```

## API

### selection_sort(array)

> Returns a sorted array

##### Params:

- `array`: Unsorted Array
