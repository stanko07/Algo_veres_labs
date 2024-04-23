import unittest
from src.the_most_k_element import search_the_largest_k


class TestQuickSort(unittest.TestCase):
    def test_sorted_array(self):
        self.assertEqual(search_the_largest_k([1, 22, 3, 43, 5], 2), (22, 1))

    def test_reverse_sorted_array(self):
        self.assertEqual(search_the_largest_k([5, 4, 3, 2, 1], 3), (3, 2))

    def test_minus_el_in_array(self):
        self.assertEqual(search_the_largest_k([4, 3, 51, -2, 10, ], 2), (10, 4))

    def test_none_in_array(self):
        self.assertEqual(search_the_largest_k([], 3), None)

    def test_length_of_arr_less_than_k(self):
        self.assertEqual(search_the_largest_k([4, 2, 5, 10, 11, 12], 8), None)

    def test_k5_of_arr_k(self):
        self.assertEqual(search_the_largest_k([1, 7, -1, 2, 9, 21, 5, 8, 9, 25], 2), (21,5))


if __name__ == '__main__':
    unittest.main()
