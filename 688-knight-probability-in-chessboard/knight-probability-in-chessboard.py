class Solution(object):
    def knightProbability(self, n, k, row, column):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        moves = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]
        dp = [[0.0] * n for _ in range(n)]
        dp[row][column] = 1.0
        for _ in range(k):
            new_dp = [[0.0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    if dp[r][c] == 0.0:
                        continue  
                    prob = dp[r][c] / 8.0  
                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            new_dp[nr][nc] += prob
            dp = new_dp
        return sum(sum(row_probs) for row_probs in dp)
if __name__ == "__main__":
    solution = Solution()
    result1 = solution.knightProbability(3, 2, 0, 0)
    print("Example 1:")
    print("Input:  n = 3, k = 2, row = 0, column = 0")
    print("Output:", result1)
    print("Expected: 0.0625")
    print()
    result2 = solution.knightProbability(1, 0, 0, 0)
    print("Example 2:")
    print("Input:  n = 1, k = 0, row = 0, column = 0")
    print("Output:", result2)
    print("Expected: 1.0")
    print()
    result3 = solution.knightProbability(8, 0, 3, 4)
    print("Example 3 (extra):")
    print("Input:  n = 8, k = 0, row = 3, column = 4")
    print("Output:", result3)
    print("Expected: 1.0")
    print()
    result4 = solution.knightProbability(3, 5, 0, 0)
    print("Example 4 (extra):")
    print("Input:  n = 3, k = 5, row = 0, column = 0")
    print("Output:", result4)
    print()
    result5 = solution.knightProbability(8, 10, 4, 4)
    print("Example 5 (extra):")
    print("Input:  n = 8, k = 10, row = 4, column = 4")
    print("Output:", result5)
print(__name__)