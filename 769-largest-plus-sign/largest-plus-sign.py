class Solution(object):
    def orderOfLargestPlusSign(self, n, mines):
        """
        :type n: int
        :type mines: List[List[int]]
        :rtype: int
        """
        mines_set = set(map(tuple, mines))
        dp = [[n] * n for _ in range(n)]
        for i in range(n):
            count = 0
            for j in range(n):
                count = 0 if (i, j) in mines_set else count + 1
                dp[i][j] = min(dp[i][j], count)
        for i in range(n):
            count = 0
            for j in range(n - 1, -1, -1):
                count = 0 if (i, j) in mines_set else count + 1
                dp[i][j] = min(dp[i][j], count)
        for j in range(n):
            count = 0
            for i in range(n):
                count = 0 if (i, j) in mines_set else count + 1
                dp[i][j] = min(dp[i][j], count)
        for j in range(n):
            count = 0
            for i in range(n - 1, -1, -1):
                count = 0 if (i, j) in mines_set else count + 1
                dp[i][j] = min(dp[i][j], count)
        return max(max(row) for row in dp)
if __name__ == "__main__":
    sol = Solution()
    n, mines = 5, [[4, 2]]
    print("Input: n = {}, mines = {}".format(n, mines))
    print("Output: {}".format(sol.orderOfLargestPlusSign(n, mines)))
    print("Expected: 2\n")
    n, mines = 1, [[0, 0]]
    print("Input: n = {}, mines = {}".format(n, mines))
    print("Output: {}".format(sol.orderOfLargestPlusSign(n, mines)))
    print("Expected: 0\n")
print(__name__)