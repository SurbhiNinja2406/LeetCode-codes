class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price        
        return max_profit
if __name__ == "__main__":
    sol = Solution()
    prices1 = [7, 1, 5, 3, 6, 4]
    print(sol.maxProfit(prices1)) 
    prices2 = [7, 6, 4, 3, 1]
    print(sol.maxProfit(prices2)) 
print(__name__)