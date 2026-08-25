class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        buy1 = float('-inf')
        sell1 = 0
        buy2 = float('-inf')
        sell2 = 0
        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)
        return sell2
if __name__ == "__main__":
    sol = Solution()
    prices1 = [3, 3, 5, 0, 0, 3, 1, 4]
    print(sol.maxProfit(prices1)) 
    prices2 = [1, 2, 3, 4, 5]
    print(sol.maxProfit(prices2))  
    prices3 = [7, 6, 4, 3, 1]
    print(sol.maxProfit(prices3)) 
print(__name__)