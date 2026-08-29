class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        cash = 0
        hold = -prices[0]
        for i in range(1, n):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([1, 3, 2, 8, 4, 9], 2))
    print("Expected: 8\n")
    print(sol.maxProfit([1, 3, 7, 5, 10, 3], 3))
    print("Expected: 6\n")
    print(sol.maxProfit([5], 1))
    print("Expected: 0\n")
    print(sol.maxProfit([9, 7, 5, 3, 1], 1))
    print("Expected: 0\n")
    print(sol.maxProfit([1, 5], 10))
    print("Expected: 0\n")
    print(sol.maxProfit([1, 10], 2))
    print("Expected: 7")
print(__name__)