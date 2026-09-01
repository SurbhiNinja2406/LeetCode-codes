import heapq
from collections import defaultdict


class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {}
        min_heap = [(0, k)]
        while min_heap:
            d, node = heapq.heappop(min_heap)
            if node in dist:
                continue
            dist[node] = d
            for neighbor, weight in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(min_heap, (d + weight, neighbor))
        if len(dist) != n:
            return -1
        return max(dist.values())
if __name__ == "__main__":
    solution = Solution()
    times1 = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n1, k1 = 4, 2
    result1 = solution.networkDelayTime(times1, n1, k1)
    print("Example 1: Output = {0}, Expected = 2".format(result1))
    assert result1 == 2
    times2 = [[1, 2, 1]]
    n2, k2 = 2, 1
    result2 = solution.networkDelayTime(times2, n2, k2)
    print("Example 2: Output = {0}, Expected = 1".format(result2))
    assert result2 == 1
    times3 = [[1, 2, 1]]
    n3, k3 = 2, 2
    result3 = solution.networkDelayTime(times3, n3, k3)
    print("Example 3: Output = {0}, Expected = -1".format(result3))
    assert result3 == -1
    print("\nAll test cases passed!")