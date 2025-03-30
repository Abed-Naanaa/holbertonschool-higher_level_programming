#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 5, 100, -50]), 100)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_all_same_numbers(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_large_numbers(self):
        self.assertEqual(max_integer([1000000, 500000, 1000001]), 1000001)

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 2.9]), 3.3)

    def test_mixed_int_float(self):
        self.assertEqual(max_integer([1, 2.5, 3, 4.8]), 4.8)

    def test_string(self):
        self.assertEqual(max_integer("hello"), "o")

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

if __name__ == '__main__':
    unittest.main()
