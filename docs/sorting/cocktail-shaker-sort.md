# Cocktail Shaker Sort

Cocktail shaker sort, also known as bidirectional bubble sort, cocktail sort, shaker sort (which can also refer to a variant of selection sort), ripple sort, shuffle sort, or shuttle sort, is a variation of bubble sort that is both a stable sorting algorithm and a comparison sort. The algorithm differs from a bubble sort in that it sorts in both directions on each pass through the list. This sorting algorithm is only marginally more difficult to implement than a bubble sort, and solves the problem of turtles in bubble sorts. It provides only marginal performance improvements, and does not improve asymptotic performance; like the bubble sort, it is not of practical interest (insertion sort is preferred for simple sorts), though it finds some use in education.

## Install

```
pip install allalgorithms
```

## Usage

```py
from allalgorithms.sorting import cocktail_shaker_sort

arr = [77, 2, 10, -2, 1, 7]

print(cocktail_shaker_sort(arr))
# -> [-2, 1, 2, 7, 10, 77]
```

## API

### cocktail_shaker_sort(array)

> Returns a sorted array

##### Params:

- `array`: Unsorted Array
