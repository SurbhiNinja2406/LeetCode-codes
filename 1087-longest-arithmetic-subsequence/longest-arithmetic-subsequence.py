class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [{} for _ in range(n)]
        max_length = 1 
        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]
                dp[i][d] = dp[j].get(d, 1) + 1
                max_length = max(max_length, dp[i][d])
        return max_length
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([3, 6, 9, 12], 4),
        ([9, 4, 7, 2, 10], 3),
        ([20, 1, 15, 3, 10, 5, 8], 4),
        ([1, 2], 2),
        ([1, 5, 7, 8, 5, 3, 4, 2, 1], 4),
    ]
    for nums, expected in test_cases:
        result = sol.longestArithSeqLength(nums)
        status = "PASS" if result == expected else "FAIL"
        print("nums={0} -> {1} (expected {2}) [{3}]".format(
            nums, result, expected, status
        ))
print(__name__)