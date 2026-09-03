class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        INF = float('inf')
        dist = [INF] * n
        dist[src] = 0
        for _ in range(k + 1):
            temp = dist[:]  
            for u, v, price in flights:
                if dist[u] != INF and dist[u] + price < temp[v]:
                    temp[v] = dist[u] + price
            dist = temp
        return dist[dst] if dist[dst] != INF else -1
if __name__ == "__main__":
    sol = Solution()
    n1 = 4
    flights1 = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    src1, dst1, k1 = 0, 3, 1
    result1 = sol.findCheapestPrice(n1, flights1, src1, dst1, k1)
    print("Example 1: {} (Expected: 700)".format(result1))
    n2 = 3
    flights2 = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src2, dst2, k2 = 0, 2, 1
    result2 = sol.findCheapestPrice(n2, flights2, src2, dst2, k2)
    print("Example 2: {} (Expected: 200)".format(result2))
    n3 = 3
    flights3 = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src3, dst3, k3 = 0, 2, 0
    result3 = sol.findCheapestPrice(n3, flights3, src3, dst3, k3)
    print("Example 3: {} (Expected: 500)".format(result3))
    n4 = 3
    flights4 = [[0, 1, 100]]
    src4, dst4, k4 = 0, 2, 1
    result4 = sol.findCheapestPrice(n4, flights4, src4, dst4, k4)
    print("Example 4 (no route): {} (Expected: -1)".format(result4))
    n5 = 5
    flights5 = [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]]
    src5, dst5, k5 = 0, 2, 2
    result5 = sol.findCheapestPrice(n5, flights5, src5, dst5, k5)
    print("Example 5: {} (Expected: 7)".format(result5))
print(__name__)