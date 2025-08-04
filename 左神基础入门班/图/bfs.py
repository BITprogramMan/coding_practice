def bfs(node):
    if not node:
        return None
    from collections import deque
    queue = deque([node])
    visited = set([node])
    while queue:
        node = queue.popleft()
        print(node.val)
        for next_node in node.nexts:
            if next_node not in visited:
                queue.append(next_node)
                visited.add(node)

