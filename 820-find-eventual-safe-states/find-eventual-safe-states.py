from collections import deque


class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        reverse_adj = [[] for _ in range(n)]
        out_degree = [0] * n
        for u in range(n):
            out_degree[u] = len(graph[u])
            for v in graph[u]:
                reverse_adj[v].append(u)
        queue = deque(u for u in range(n) if out_degree[u] == 0)
        is_safe = [False] * n
        while queue:
            node = queue.popleft()
            is_safe[node] = True
            for parent in reverse_adj[node]:
                out_degree[parent] -= 1
                if out_degree[parent] == 0:
                    queue.append(parent)
        return [u for u in range(n) if is_safe[u]]
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([[1, 2], [2, 3], [5], [0], [5], [], []], [2, 4, 5, 6]),
        ([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []], [4]),
    ]
    for graph, expected in test_cases:
        result = solution.eventualSafeNodes([list(edges) for edges in graph])
        status = "PASS" if result == expected else "FAIL"
        print("graph={:<35} expected={:<15} got={:<15} [{}]".format(
            str(graph), str(expected), str(result), status))
print(__name__)