from collections import deque

def level_order_traversal(root):
  result = []
  if root is None:
    return result
  queue = deque()
  queue.append(root)

  while queue:
    node = queue.popleft()
    result.append(node.value)

    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)

  return result
