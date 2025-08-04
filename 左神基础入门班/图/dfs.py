def dfs(node):
    if not node:
        return None
    stack = [node]
    visited = set([node])
    while stack:
        node = stack.pop()
        print(node.val)
        for next_node in node.nexts:
            if next_node not in visited:
                stack.append(node)
                stack.append(next_node)
                visited.add(next_node)
                break


