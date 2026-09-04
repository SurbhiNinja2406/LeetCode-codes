class Solution(object):
    def largestSumOfAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        prefix = [0.0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        def avg(m, i):
            return (prefix[i] - prefix[m]) / float(i - m)
        dp = [0.0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = avg(0, i)
        for j in range(2, k + 1):
            new_dp = [0.0] * (n + 1)
            for i in range(1, n + 1):
                best = 0.0
                for m in range(j - 1, i):
                    candidate = dp[m] + avg(m, i)
                    if candidate > best:
                        best = candidate
                new_dp[i] = best
            dp = new_dp
        return dp[n]
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([9, 1, 2, 3, 9], 3, 20.00000),
        ([1, 2, 3, 4, 5, 6, 7], 4, 20.50000),
    ]
    for nums, k, expected in test_cases:
        result = solution.largestSumOfAverages(list(nums), k)
        status = "PASS" if abs(result - expected) < 1e-6 else "FAIL"
        print("nums={:<25} k={} expected={:<10.5f} got={:<10.5f} [{}]".format(
            str(nums), k, expected, result, status))
print(__name__)