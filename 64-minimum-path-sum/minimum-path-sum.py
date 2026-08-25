class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0        
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]
        for col in range(1, n):
            dp[col] = dp[col - 1] + grid[0][col]
        for row in range(1, m):
            for col in range(n):
                if col == 0:
                    dp[col] = dp[col] + grid[row][col]
                else:
                    dp[col] = min(dp[col], dp[col - 1]) + grid[row][col]        
        return dp[n - 1]
if __name__ == "__main__":
    solution = Solution()
    grid1 = [[1,3,1],[1,5,1],[4,2,1]]
    print(solution.minPathSum(grid1))  
    grid2 = [[1,2,3],[4,5,6]]
    print(solution.minPathSum(grid2)) 
print(__name__)