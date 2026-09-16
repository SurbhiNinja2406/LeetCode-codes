class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        travel_days = set(days)
        last_day = days[-1]
        dp = [0] * (last_day + 31)  
        for d in range(last_day, 0, -1):
            if d not in travel_days:
                dp[d] = dp[d + 1]
            else:
                one_day = costs[0] + dp[d + 1]
                seven_day = costs[1] + dp[d + 7]
                thirty_day = costs[2] + dp[d + 30]
                dp[d] = min(one_day, seven_day, thirty_day)
        return dp[1]
if __name__ == "__main__":
    sol = Solution()
    print(sol.mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))          
    print(sol.mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]))  
print(__name__)
        