import unittest

from allalgorithms.string import palindrome_check


class TestSorting(unittest.TestCase):

    def test_palindrome_check(self):
        self.assertEqual(True, palindrome_check("a"))
        self.assertEqual(True, palindrome_check("10201"))
        self.assertEqual(False, palindrome_check("test"))
        self.assertEqual(True, palindrome_check("Mr. Owl ate my metal worm"))
        self.assertEqual(True, palindrome_check("Was it a car or a cat I saw?"))
        self.assertEqual(False, palindrome_check("How are you?"))

if __name__ == "__main__":
    unittest.main()
