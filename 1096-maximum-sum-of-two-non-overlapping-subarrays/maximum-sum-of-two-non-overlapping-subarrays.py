class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        def helper(L, M):
            best = 0
            max_L = 0
            for i in range(L + M, n + 1):
                max_L = max(max_L, prefix[i - M] - prefix[i - M - L])
                best = max(best, max_L + prefix[i] - prefix[i - M])
            return best
        return max(helper(firstLen, secondLen), helper(secondLen, firstLen))
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2, 20),
        ([3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2, 29),
        ([2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4, 3, 31),
    ]
    for nums, f, s, expected in tests:
        result = sol.maxSumTwoNoOverlap(nums, f, s)
        status = "PASS" if result == expected else "FAIL"
        print("{}: got {}, expected {}".format(status, result, expected))
print(__name__)