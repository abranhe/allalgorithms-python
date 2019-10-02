# Selection Sort

In computer science, shell sort improves upon insertion sort by moving out of order elements more than one position at a time. It has a best case O(n log n) time complexity, and for other cases, it depends on the gap sequence. According to Poonen Theorem, worst case complexity for shell sort is Θ(NlogN)^2/(log logN)^2) or Θ(NlogN)^2/log logN) or Θ(N(logN)^2) or something in between.
## Install

```
pip install allalgorithms
```

## Usage

```py
from allalgorithms.sorting import shell_sort

arr = [77, 2, 10, -2, 1, 7]

print(shell_sort(arr))
# -> [-2, 1, 2, 7, 10, 77]
```

## API

### selection_sort(array)

> Returns a sorted array

##### Params:

- `array`: Unsorted Array
