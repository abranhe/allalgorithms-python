# Pigeonhole Sort

Pigeonhole sorting is a sorting algorithm that is suitable for sorting lists of elements where the number of elements (n) and the length of the range of possible key values (N) are approximately the same. It requires O(n + N) time. It is similar to counting sort, but differs in that it "moves items twice: once to the bucket array and again to the final destination [whereas] counting sort builds an auxiliary array then uses the array to compute each item's final destination and move the item there."

## Install

```
pip install allalgorithms
```

## Usage

```py
from allalgorithms.sorting import pigeonhole_sort

arr = [77, 2, 10, -2, 1, 7]

print(pigeonhole_sort(arr))
# -> [-2, 1, 2, 7, 10, 77]
```

## API

### pigeonhole_sort(array)

> Returns a sorted array

##### Params:

- `array`: Unsorted Array
