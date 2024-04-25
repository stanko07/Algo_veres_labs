import unittest
from src.the_shortest_safe_route import shortest_path, transform_matrix


class TestShortestPath(unittest.TestCase):
    def test_shortest_path_matrix(self):
        matrix_test = [
            [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

        transformed_matrix_custom = transform_matrix(matrix_test)
        expected_length_custom = 11
        expected_path_custom = [
            (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
            (2, 5), (2, 6), (1, 6), (0, 6), (0, 7),
            (0, 8), (0, 9)
        ]
        result_length_custom, result_path_custom = shortest_path(transformed_matrix_custom)
        self.assertEqual(result_length_custom, expected_length_custom)
        self.assertEqual(result_path_custom, expected_path_custom)


if __name__ == '__main__':
    unittest.main()
