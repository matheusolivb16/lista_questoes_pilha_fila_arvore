class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_strict_binary_tree(root):
    if not root:
        return True

    if root.left and not root.right:
        return False

    if root.right and not root.left:
        return False

    return is_strict_binary_tree(root.left) and is_strict_binary_tree(root.right)
