#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function"""

    def test_ordered_list(self):
        """max is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """max is in the middle"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_start(self):
        """max is at the beginning"""
        self.assertEqual(max_integer([9, 3, 4, 2]), 9)

    def test_single_element(self):
        """list with only one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """empty list returns None"""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """default argument is an empty list, returns None"""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """list of negative numbers"""
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)

    def test_mixed_positive_negative(self):
        """list with both positive and negative numbers"""
        self.assertEqual(max_integer([-10, 5, 3, -2, 8]), 8)

    def test_all_same_values(self):
        """list where all values are the same"""
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_two_elements(self):
        """list with exactly two elements"""
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([2, 1]), 2)

    def test_floats(self):
        """list containing floats"""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_max_is_zero(self):
        """max value is zero"""
        self.assertEqual(max_integer([-5, -3, 0, -1]), 0)

    def test_duplicate_max(self):
        """max value appears more than once"""
        self.assertEqual(max_integer([3, 9, 9, 2]), 9)

    def test_large_list(self):
        """large list of numbers"""
        self.assertEqual(max_integer(list(range(1000))), 999)


if __name__ == '__main__':
    unittest.main()
