import unittest

from allalgorithms.sorting import (
    binary_search,
    fibonacci_search
)

class TestSearches(unittest.TestCase):

	def test_binary_search(self):
		arr = [1, 2, 3, 7, 10, 19, 27, 77]
		self.assertEqual(3, binary_search(arr, 7))
		self.assertEqual(7, binary_search(arr, 77))
		self.assertEqual(None, binary_search(arr, 8))
		self.assertEqual(None, binary_search(arr, -1))

	def test_fibonacci_search(self):
		arr = [1, 2, 3, 7, 10, 19, 27, 77]
		self.assertEqual(3, fibonacci_search(arr, 7))
		self.assertEqual(7, fibonacci_search(arr, 77))
		self.assertEqual(None, fibonacci_search(arr, 8))
		self.assertEqual(None, fibonacci_search(arr, -1))


if __name__ == '__main__':
	unittest.main()
