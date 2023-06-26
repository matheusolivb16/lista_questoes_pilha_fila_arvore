def is_complete_tree(root):
    if not root:
        return True

    queue = [root]
    flag = False

    while len(queue) > 0:
        curr = queue.pop(0)

        if curr.left:
            if flag:
                return False
            queue.append(curr.left)
        else:
            flag = True

        if curr.right:
            if flag:
                return False
            queue.append(curr.right)
        else:
            flag = True

    return True

