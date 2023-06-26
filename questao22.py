class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traversal(root):
        result = [root.value]
        result += preorder_traversal(root.left)
        result += preorder_traversal(root.right)
        return result