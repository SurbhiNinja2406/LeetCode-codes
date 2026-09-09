import heapq

class Solution(object):
    def reachableNodes(self, edges, maxMoves, n):
        """
        :type edges: List[List[int]]
        :type maxMoves: int
        :type n: int
        :rtype: int
        """
        graph = [[] for _ in range(n)]
        for u, v, cnt in edges:
            graph[u].append((v, cnt))
            graph[v].append((u, cnt))
        dist = [float('inf')] * n
        dist[0] = 0
        visited = [False] * n
        heap = [(0, 0)]  
        while heap:
            d, node = heapq.heappop(heap)
            if visited[node]:
                continue
            visited[node] = True
            for neighbor, cnt in graph[node]:
                new_dist = d + cnt + 1
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))
        reachable_original = sum(1 for d in dist if d <= maxMoves)
        total_subdivided_reachable = 0
        for u, v, cnt in edges:
            a = max(0, maxMoves - dist[u]) if dist[u] <= maxMoves else 0
            a = min(a, cnt)
            b = max(0, maxMoves - dist[v]) if dist[v] <= maxMoves else 0
            b = min(b, cnt)
            total_subdivided_reachable += min(cnt, a + b)
        return reachable_original + total_subdivided_reachable
if __name__ == "__main__":
    sol = Solution()
    edges1 = [[0, 1, 10], [0, 2, 1], [1, 2, 2]]
    maxMoves1, n1 = 6, 3
    result1 = sol.reachableNodes(edges1, maxMoves1, n1)
    print("Example 1: {} (expected 13)".format(result1))
    edges2 = [[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]]
    maxMoves2, n2 = 10, 4
    result2 = sol.reachableNodes(edges2, maxMoves2, n2)
    print("Example 2: {} (expected 23)".format(result2))
    edges3 = [[1, 2, 4], [1, 4, 5], [1, 3, 1], [2, 3, 4], [3, 4, 5]]
    maxMoves3, n3 = 17, 5
    result3 = sol.reachableNodes(edges3, maxMoves3, n3)
    print("Example 3: {} (expected 1)".format(result3))
print(__name__)