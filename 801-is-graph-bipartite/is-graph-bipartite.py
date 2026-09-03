from collections import deque
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        color = [0] * n  
        for start in range(n):
            if color[start] != 0:
                continue
            color[start] = 1
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = -color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False
        return True
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], False),
        ([[1, 3], [0, 2], [1, 3], [0, 2]], True),
        ([[]], True),
        ([[1], [0]], True),
    ]
    for i, (graph, expected) in enumerate(test_cases, 1):
        result = sol.isBipartite(graph)
        status = "PASS" if result == expected else "FAIL"
        print("Test " + str(i) + ": graph=" + str(graph) +
              " -> got=" + str(result) + ", expected=" + str(expected) +
              " [" + status + "]")
print(__name__)