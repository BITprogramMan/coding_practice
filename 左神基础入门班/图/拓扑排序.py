def topologySort(graph):
    inMap = dict()
    from collections import deque
    zeroInQueue = deque()
    for node in graph.nodes.values:
        inMap[node] = node.in_
        if inMap[node] == 0:
            zeroInQueue.append(node)
    res = []
    while zeroInQueue:
        node = zeroInQueue.popleft()
        res.append(node)
        for next_node in node.nexts:
            inMap[next_node] -= 1
            if inMap[next_node] == 0:
                zeroInQueue.append(next_node)
    return res

