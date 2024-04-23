import unittest
from src.swap_binary_tree import BinaryTree, invert_binary_tree


class TestForTree(unittest.TestCase):

    def setUp(self):
        """
        Добавлення значень для тесту
        """
        self.root = BinaryTree(1)
        self.root.left = BinaryTree(2)
        self.root.right = BinaryTree(3)
        self.root.left.left = BinaryTree(4)
        self.root.left.right = BinaryTree(5)
        self.root.right.left = BinaryTree(6)
        self.root.right.right = BinaryTree(7)

    def test_inverting_tree(self):
        """
        Тест для функції invert_binary_tree
        """
        invert_binary_tree(self.root)
        self.assertEqual(self.root.value, 1)
        self.assertEqual(self.root.left.value, 3)
        self.assertEqual(self.root.right.value, 2)
        self.assertEqual(self.root.left.left.value, 7)
        self.assertEqual(self.root.left.right.value, 6)
        self.assertEqual(self.root.right.left.value, 5)
        self.assertEqual(self.root.right.right.value, 4)


if __name__ == '__main__':
    unittest.main()
