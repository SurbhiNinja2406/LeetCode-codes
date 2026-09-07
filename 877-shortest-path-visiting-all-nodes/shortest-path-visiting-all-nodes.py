from collections import deque
class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        if n == 1:
            return 0
        full_mask = (1 << n) - 1
        visited = set()
        queue = deque()
        for i in range(n):
            mask = 1 << i
            queue.append((i, mask, 0)) 
            visited.add((i, mask))
        while queue:
            node, mask, dist = queue.popleft()
            if mask == full_mask:
                return dist
            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)
                state = (neighbor, new_mask)
                if state not in visited:
                    visited.add(state)
                    queue.append((neighbor, new_mask, dist + 1))
        return -1 
if __name__ == "__main__":
    solution = Solution()
    graph1 = [[1, 2, 3], [0], [0], [0]]
    print(solution.shortestPathLength(graph1)) 
    graph2 = [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]
    print(solution.shortestPathLength(graph2))  
    graph3 = [[]]
    print(solution.shortestPathLength(graph3)) 
    graph4 = [[1], [0]]
    print(solution.shortestPathLength(graph4)) 
    graph5 = [[1], [0, 2], [1, 3], [2]]
    print(solution.shortestPathLength(graph5)) 
    graph6 = [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]]
    print(solution.shortestPathLength(graph6))  
print(__name__)