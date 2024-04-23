class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value, priority):
        if not self.root:
            self.root = Node(value, priority)
            return
        self.__add(value, priority, self.root)

    def __add(self, value, priority, node):
        if node.priority >= priority:
            if not node.left:
                node.left = Node(value, priority)
            else:
                self.__add(value, priority, node.left)
        else:
            if not node.right:
                node.right = Node(value, priority)
            else:
                self.__add(value, priority, node.right)

    def delete(self):
        node_to_delete = self.search()
        parent = node_to_delete[0]
        parent.right = node_to_delete[1].left
        return node_to_delete[1].priority

    def search(self):
        node = self.root
        while node.right.right:
            node = node.right
        return node, node.right

    def inorder_tree(self, node):
        if node is None:
            return

        self.inorder_tree(node.right)
        print(node.priority)
        self.inorder_tree(node.left)


binary = BinaryTree()
binary.add(5, 5)
binary.add(50, 4)
binary.add(30, 3)
binary.add(30, 6)
binary.add(30, 10)
binary.add(30, 12)
binary.add(30, 9)
binary.add(30, 5)
binary.add(30, 3)
binary.add(30, 1)

binary.inorder_tree(binary.root)
print("Delete priority:", binary.delete())
binary.inorder_tree(binary.root)