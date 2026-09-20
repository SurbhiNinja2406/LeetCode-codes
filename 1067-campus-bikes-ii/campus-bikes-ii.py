class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: int
        """
        n, m = len(workers), len(bikes)
        def dist(w, b):
            return abs(workers[w][0] - bikes[b][0]) + abs(workers[w][1] - bikes[b][1])
        INF = float('inf')
        dp = [INF] * (1 << m)
        dp[0] = 0
        answer = INF
        for mask in range(1 << m):
            if dp[mask] == INF:
                continue
            worker = bin(mask).count('1')
            if worker == n:
                answer = min(answer, dp[mask])
                continue
            for bike in range(m):
                if mask & (1 << bike):
                    continue
                new_mask = mask | (1 << bike)
                cost = dp[mask] + dist(worker, bike)
                if cost < dp[new_mask]:
                    dp[new_mask] = cost
        return answer
if __name__ == "__main__":
    sol = Solution()
    print(sol.assignBikes([[0, 0], [2, 1]],
                          [[1, 2], [3, 3]]))          
    print(sol.assignBikes([[0, 0], [1, 1], [2, 0]],
                          [[1, 0], [2, 2], [2, 1]]))           
    print(sol.assignBikes([[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]],
                          [[0, 999], [1, 999], [2, 999], [3, 999], [4, 999]]))
print(__name__)