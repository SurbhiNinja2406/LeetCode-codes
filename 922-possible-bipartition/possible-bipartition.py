from collections import deque

class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(n + 1)]
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        color = [0] * (n + 1)
        for start in range(1, n + 1):
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
    n1, dislikes1 = 4, [[1, 2], [1, 3], [2, 4]]
    result1 = sol.possibleBipartition(n1, dislikes1)
    print("Example 1: {} (expected True)".format(result1))
    n2, dislikes2 = 3, [[1, 2], [1, 3], [2, 3]]
    result2 = sol.possibleBipartition(n2, dislikes2)
    print("Example 2: {} (expected False)".format(result2))