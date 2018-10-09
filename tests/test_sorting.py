import unittest

from allalgorithms.sorting import (bubble_sort,
                                   insertion_sort,
                                   merge_sort,
                                   selection_sort)


class TestSorting(unittest.TestCase):
    def test_merge_sort(self):
        self.assertEqual([-44, 1, 2, 3, 7, 19], merge_sort([7, 3, 2, 19, -44, 1]))

    def test_bubble_sort(self):
        self.assertEqual([-44, 1, 2, 3, 7, 19], bubble_sort([7, 3, 2, 19, -44, 1]))

    def test_insertion_sort(self):
        self.assertEqual([-44, 1, 2, 3, 7, 19], insertion_sort([7, 3, 2, 19, -44, 1]))

    def test_selection_sort(self):
        self.assertEqual([-44, 1, 2, 3, 7, 19], selection_sort([7, 3, 2, 19, -44, 1]))


if __name__ == "__main__":
    unittest.main()
