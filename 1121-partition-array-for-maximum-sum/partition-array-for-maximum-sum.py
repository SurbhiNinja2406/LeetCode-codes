class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            cur_max = 0
            for j in range(1, min(k, i) + 1):
                cur_max = max(cur_max, arr[i - j])    
                dp[i] = max(dp[i], dp[i - j] + cur_max * j)  
        return dp[n]
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 15, 7, 9, 2, 5, 10], 3, 84),
        ([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4, 83),
        ([1], 1, 1),
    ]
    for arr, k, expected in tests:
        result = sol.maxSumAfterPartitioning(arr, k)
        status = "PASS" if result == expected else "FAIL"
        print("{}: got {}, expected {}".format(status, result, expected))
print(__name__)