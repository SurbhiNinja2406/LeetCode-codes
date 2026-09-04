class Solution(object):
    def splitArraySameAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 2:
            return False
        total = sum(nums)
        dp = [0] * (n + 1)
        dp[0] = 1  
        for num in nums:
            for k in range(n, 0, -1):
                dp[k] |= dp[k - 1] << num
        max_k = n // 2  
        for k in range(1, max_k + 1):
            if (total * k) % n != 0:
                continue
            target = (total * k) // n
            if (dp[k] >> target) & 1:
                return True
        return False
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7, 8], True),
        ([3, 1], False),
    ]
    for nums, expected in test_cases:
        result = solution.splitArraySameAverage(list(nums))
        status = "PASS" if result == expected else "FAIL"
        print("nums={:<25} expected={} got={} [{}]".format(
            str(nums), expected, result, status))
print(__name__)