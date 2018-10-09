# Bubble Sort

Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted. The algorithm, which is a comparison sort, is named for the way smaller or larger elements "bubble" to the top of the list. Although the algorithm is simple, it is too slow and impractical for most problems even when compared to insertion sort. Bubble sort can be practical if the input is in mostly sorted order with some out-of-order elements nearly in position.

## Install

```
pip install allalgorithms
```

## Usage

```py
from allalgorithms.sorting import bubble_sort

arr = [77, 2, 10, -2, 1, 7]

print(bubble_sort(arr))
# -> [-2, 1, 2, 7, 10, 77]
```

## API

### bubble_sort(array)

> Returns a sorted array

##### Params:

- `array`: Unsorted Array
