# Fibonacci Search

In computer science, the Fibonacci search technique is a method of searching a sorted array using a divide and conquer algorithm that narrows down possible locations with the aid of Fibonacci numbers. (Wikipedia)
## Install

```
pip install allalgorithms
```

## Usage

```py
from allalgorithms.searches import fibonacci_search

arr = [-2, 1, 2, 7, 10, 77]

print(fibonacci_search(arr, 7))
# -> 3

print(fibonacci_search(arr, 3))
# -> None
```

## API

### fibonacci_search(array, query)

> Return array index if its found, otherwise returns `None`

##### Params:

- `array`: Sorted Array
- `query`: Element to search for in the array
