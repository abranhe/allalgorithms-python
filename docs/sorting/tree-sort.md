# Tree Sort

A tree sort is a sort algorithm that builds a binary search tree from the elements to be sorted, and then traverses the tree (in-order) so that the elements come out in sorted order. It has two phases:
1. Frist is creating a binary search tree using the given array elements.
2. Second phase is traversing the given binary search tree in inorder, thus resulting in a sorted array.

**Performance**

The average number of comparisions for this method is O(nlogn). But in worst case, number of comparisions is reduced by O(n^2), a case which arrives when the tree is skewed.



## Install

```
pip install allalgorithms
```

## Usage

```py
from allalgorithms.sorting import tree_sort

arr = [77, 2, 10, -2, 1, 7]

print(tree_sort(arr))
# -> [-2, 1, 2, 7, 10, 77]
```

## API

### tree_sort(array)

> Returns a sorted array

##### Params:

- `array`: Unsorted Array