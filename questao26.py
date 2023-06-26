class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def height(node):
    left_height = height(node.left)
    right_height = height(node.right)
    return max(left_height, right_height) + 1
