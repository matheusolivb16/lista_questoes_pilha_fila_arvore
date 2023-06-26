def count_nodes(root):
    if root is None:
        return 0
    
    count_left = count_nodes(root.left)
    count_right = count_nodes(root.right)
    
    return count_left + count_right + 1