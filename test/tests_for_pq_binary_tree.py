from src.pq_binary_tree import *
import unittest


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree()

    def test_add(self):
        self.tree.add(5, 5)
        self.assertEqual(self.tree.root.priority, 5)
        self.tree.add(3, 3)
        self.assertEqual(self.tree.root.left.priority, 3)
        self.tree.add(7, 7)
        self.assertEqual(self.tree.root.right.priority, 7)
        self.tree.add(3, 6)
        self.assertEqual(self.tree.root.right.left.priority, 6)

    def test_delete(self):
        self.tree.add(5, 5)
        self.tree.add(3, 3)
        self.tree.add(7, 7)
        self.tree.add(3, 6)
        self.tree.add(24, 2)
        self.tree.add(3, 1)
        self.assertEqual(self.tree.delete(), 7)


if __name__ == '__main__':
    unittest.main()
