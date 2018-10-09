# Insertion Sort

Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

## Install

```
pip install allalgorithms
```

## Usage

```py
from allalgorithms.sorting import insertion_sort

arr = [77, 2, 10, -2, 1, 7]

print(insertion_sort(arr))
# -> [-2, 1, 2, 7, 10, 77]
```

## API

### insertion_sort(array)

> Returns a sorted array

##### Params:

- `array`: Unsorted Array
