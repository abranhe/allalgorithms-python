# Jump Search

In computer science, jump search is a search algorithm for sorted array which find the element by jumping ahead by fixed steps or skipping some elements in place of searching all elements.

## Install

```
pip install allalgorithms
```

## Usage

```py
from allalgorithms.searches import jump_search

arr = [-2, 1, 2, 7, 10, 77]

print(jump_search(arr, 7))
# -> 3

print(jump_search(arr, 3))
# -> None
```

## API

### jump_search(array, query)

> Return array index if its found, otherwise returns `None`

##### Params:

- `arr`: Sorted Array
- `query`: Element to search for in the array


