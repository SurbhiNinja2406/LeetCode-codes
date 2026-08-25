class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[m][n - 1] = 1
        dp[m - 1][n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                min_health_needed_after = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(1, min_health_needed_after - dungeon[i][j])
        return dp[0][0]
if __name__ == "__main__":
    sol = Solution()
    print(sol.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))  
    print(sol.calculateMinimumHP([[0]]))  