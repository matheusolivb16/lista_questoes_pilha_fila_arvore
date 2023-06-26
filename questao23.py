def inorder_traversal(root):
    result = []
    if root is not None:
        result += inorder_traversal(root.left)
        result.append(root.value)
        result += inorder_traversal(root.right)
    return result