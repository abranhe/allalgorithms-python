import unittest

from allalgorithms.sorting import (
    bubble_sort,
    insertion_sort,
    merge_sort,
    selection_sort,
    pidgeonhole_sort,
    stooge_sort,
    cocktail_shaker_sort
)


class TestSorting(unittest.TestCase):
    def test_merge_sort(self):
        self.assertEqual([-44, 1, 2, 3, 7, 19], merge_sort([7, 3, 2, 19, -44, 1]))

    def test_bubble_sort(self):
        self.assertEqual([-44, 1, 2, 3, 7, 19], bubble_sort([7, 3, 2, 19, -44, 1]))

    def test_insertion_sort(self):
        self.assertEqual([-44, 1, 2, 3, 7, 19], insertion_sort([7, 3, 2, 19, -44, 1]))

    def test_selection_sort(self):
        self.assertEqual([-44, 1, 2, 3, 7, 19], selection_sort([7, 3, 2, 19, -44, 1]))

    def test_pidgeonhole_sort(self):
        self.assertEqual([-44, 1, 2, 3, 7, 19], pidgeonhole_sort([7, 3, 2, 19, -44, 1]))

    def test_stooge_sort(self):
        self.assertEqual([-44, 1, 2, 3, 7, 19], stooge_sort([7, 3, 2, 19, -44, 1]))

    def test_cocktail_shaker_sort(self):
        self.assertEqual([-44, 1, 2, 3, 7, 19], cocktail_shaker_sort([7, 3, 2, 19, -44, 1]))


if __name__ == "__main__":
    unittest.main()
