class Node:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
        
bt = BinaryTree()
bt.root = Node(value = 1)
bt.root.left = Node()


