class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def get_leaf_nodes(root):
    leaf_nodes = []

    stack = [root]

    while len(stack) > 0:
        node = stack.pop()

        if node.left is None and node.right is None:
            leaf_nodes.append(node.value)
        else:
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)

    return leaf_nodes