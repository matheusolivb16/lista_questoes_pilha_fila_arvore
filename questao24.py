def postorder_traversal(root):
    result = []
    if root is not None:
        result += postorder_traversal(root.left)
        result += postorder_traversal(root.right)
        result.append(root.value)
    return result