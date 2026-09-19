class Solution(object):
    def minScoreTriangulation(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        for gap in range(2, n):
            for i in range(n - gap):
                j = i + gap
                best = float('inf')
                for k in range(i + 1, j):
                    cost = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]
                    if cost < best:
                        best = cost
                dp[i][j] = best
        return dp[0][n - 1]
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 3], 6),
        ([3, 7, 4, 5], 144),
        ([1, 3, 1, 4, 1, 5], 13),
    ]
    for values, expected in tests:
        result = sol.minScoreTriangulation(values)
        status = "PASS" if result == expected else "FAIL"
        print("{}: got {}, expected {}".format(status, result, expected))
print(__name__)