from src.linguistic_game import find_the_longest_chain
import unittest


class MyTestCase(unittest.TestCase):

    def test_normal_list(self):
        words = ['crates', 'car', 'cats', 'crate', 'rate', 'at', 'ate', 'tea', 'rat', 'a']
        result = find_the_longest_chain(words)
        self.assertEqual(result, 6)

    def test_another_list(self):
        words = ['b', 'bcad', 'bca', 'bad', 'bd']
        result = find_the_longest_chain(words)
        self.assertEqual(result, 4)

    def test_with_no_chain(self):
        words = ['word', 'anotherword', 'yetanotherword']
        result = find_the_longest_chain(words)
        self.assertEqual(result, 1)

    def test_empty_list(self):
        words = []
        result = find_the_longest_chain(words)
        self.assertEqual(result, None)
