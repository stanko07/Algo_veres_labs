import unittest
from Algo_veres_labs.src.monkey_eating_banana import minBanaEat


class TestForMavpa(unittest.TestCase):
    def test_find_min_bana(self):
        self.assertEqual(minBanaEat([3, 6, 7, 11], 8), 4)

    def test_find_min_bana1(self):
        self.assertEqual(minBanaEat([30, 11, 23, 4, 20], 5), 30)

    def test_find_min_bana2(self):
        self.assertEqual(minBanaEat([30, 11, 23, 4, 20], 6), 23)

    def test_find_banana_7(self):
        self.assertEqual(minBanaEat([7, 7, 7, 7, 7], 10), 4)

    def test_find_banana_4(self):
        self.assertEqual(minBanaEat([4, 4, 4, 4, 4], 9), 4)
