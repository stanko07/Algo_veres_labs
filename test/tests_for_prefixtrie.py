import unittest
from src.prefixtrie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.words = [
            "website",
            "trigger",
            "miwa",
            "mysql",
            "react",
            "flask",
            "spring"
        ]
        for word in self.words:
            self.trie.insert(word)

    def test_search_existing_words(self):
        for word in self.words:
            self.assertTrue(self.trie.search(word))

    def test_search_non_existing_word(self):
        self.assertFalse(self.trie.search("nodejs"))
        self.assertFalse(self.trie.search("angular"))
        self.assertFalse(self.trie.search("slack"))

    def test_starts_with_existing_prefix(self):
        self.assertTrue(self.trie.find_prefix("we"))
        self.assertTrue(self.trie.find_prefix("mi"))
        self.assertTrue(self.trie.find_prefix("mysq"))

    def test_starts_with_non_existing_prefix(self):
        self.assertFalse(self.trie.find_prefix("me"))
        self.assertFalse(self.trie.find_prefix("qwe"))
        self.assertFalse(self.trie.find_prefix("vfr"))