class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                take_left = piles[i] - dp[i + 1][j]
                take_right = piles[j] - dp[i][j - 1]
                dp[i][j] = max(take_left, take_right)
        return dp[0][n - 1] > 0
def build_solution_and_test(piles):
    solution = Solution()
    result = solution.stoneGame(piles)
    print("Input:  piles = {}".format(piles))
    print("Output: {}".format(result))
    print("")
if __name__ == "__main__":
    build_solution_and_test([5, 3, 4, 5])
    build_solution_and_test([3, 7, 2, 3])
    build_solution_and_test([1, 100])
print(__name__)