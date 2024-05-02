class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_leaf = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, patterns):
        cur = self.root
        for letter in patterns:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        cur.is_leaf = True

    def search(self, word):
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        if cur.is_leaf:
            return True
        else:
            return False

    def find_prefix(self, prefix):
        cur = self.root
        for letter in prefix:
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        return True


def build_tree(patterns):
    trie = Trie()
    for pattern in patterns:
        trie.insert(pattern)
    return trie
