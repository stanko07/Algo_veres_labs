class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def invert_binary_tree(root):
    if root is None:
        return 0
    else:
        invert_binary_tree(root.right)
        invert_binary_tree(root.left)
        root.right, root.left = root.left, root.right
    return root
