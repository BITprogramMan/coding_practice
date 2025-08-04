class Solution:
    def primMST(self, graph):
        import heapq
        visited_nodes = set()
        result = []
        for node in graph.nodes.values():
            if node not in visited_nodes:
                visited_nodes.add(node)
                edges = [(edge.weight, edge) for edge in node.edges]
                heapq.heapify(edges)
                while edges:
                    weight, edge = edges.pop(0)
                    if edge.to_ in visited_nodes:
                        continue
                    result.append(edge)
                    visited_nodes.add(edge.to_)
                    for next_edge in edge.to_.edges:
                        if next_edge.to_ not in visited_nodes:
                            heapq.heappush(edges, (next_edge.weight, next_edge))

        return result






