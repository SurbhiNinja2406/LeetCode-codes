class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        prev2 = 0  
        prev1 = 0 
        for i in range(2, n + 1):
            current = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
            prev2 = prev1
            prev1 = current
        return prev1
if __name__ == "__main__":
    solution = Solution()
    cost1 = [10, 15, 20]
    result1 = solution.minCostClimbingStairs(cost1)
    print("Example 1: Output = {0}, Expected = 15".format(result1))
    assert result1 == 15
    cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    result2 = solution.minCostClimbingStairs(cost2)
    print("Example 2: Output = {0}, Expected = 6".format(result2))
    assert result2 == 6
    print("\nAll test cases passed!")
print(__name__)