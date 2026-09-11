class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        dp = matrix[0][:]
        for row in range(1, n):
            new_dp = [0] * n
            for col in range(n):
                best_prev = dp[col]
                if col - 1 >= 0:
                    best_prev = min(best_prev, dp[col - 1])
                if col + 1 < n:
                    best_prev = min(best_prev, dp[col + 1])
                new_dp[col] = matrix[row][col] + best_prev
            dp = new_dp
        return min(dp)
if __name__ == "__main__":
    sol = Solution()
    print(sol.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
    print(sol.minFallingPathSum([[-19, 57], [-40, -5]]))
print(__name__)