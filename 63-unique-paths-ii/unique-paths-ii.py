class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [0] * n
        dp[0] = 1 
        for row in range(m):
            for col in range(n):
                if obstacleGrid[row][col] == 1:
                    dp[col] = 0
                elif col > 0:
                    dp[col] += dp[col - 1]
        return dp[n - 1]
if __name__ == "__main__":
    solution = Solution()
    obstacleGrid1 = [[0,0,0],[0,1,0],[0,0,0]]
    print(solution.uniquePathsWithObstacles(obstacleGrid1))  
    obstacleGrid2 = [[0,1],[0,0]]
    print(solution.uniquePathsWithObstacles(obstacleGrid2)) 
print(__name__)