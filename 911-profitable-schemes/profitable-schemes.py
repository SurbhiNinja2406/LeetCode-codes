class Solution(object):
    def profitableSchemes(self, n, minProfit, group, profit):
        """
        :type n: int
        :type minProfit: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1 
        for g, p in zip(group, profit):
            for j in range(n, g - 1, -1):
                for k in range(minProfit, -1, -1):
                    new_profit = min(minProfit, k + p)
                    dp[j][new_profit] = (dp[j][new_profit] + dp[j - g][k]) % MOD
        return sum(dp[j][minProfit] for j in range(n + 1)) % MOD
if __name__ == "__main__":
    sol = Solution()
    n1, minProfit1, group1, profit1 = 5, 3, [2, 2], [2, 3]
    result1 = sol.profitableSchemes(n1, minProfit1, group1, profit1)
    print("Example 1: {} (expected 2)".format(result1))
    n2, minProfit2, group2, profit2 = 10, 5, [2, 3, 5], [6, 7, 8]
    result2 = sol.profitableSchemes(n2, minProfit2, group2, profit2)
    print("Example 2: {} (expected 7)".format(result2))
    n3, minProfit3, group3, profit3 = 5, 0, [3, 4], [1, 2]
    result3 = sol.profitableSchemes(n3, minProfit3, group3, profit3)
    print("Example 3 (minProfit=0): {}".format(result3))
print(__name__)