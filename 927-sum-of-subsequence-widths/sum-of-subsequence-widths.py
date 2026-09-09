class Solution(object):
    def sumSubseqWidths(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD
        total = 0
        for i in range(n):
            total = (total + nums[i] * pow2[i]) % MOD
            total = (total - nums[i] * pow2[n - 1 - i]) % MOD
        return total % MOD
if __name__ == "__main__":
    sol = Solution()
    nums1 = [2, 1, 3]
    result1 = sol.sumSubseqWidths(nums1)
    print("Example 1: {} (expected 6)".format(result1))
    nums2 = [2]
    result2 = sol.sumSubseqWidths(nums2)
    print("Example 2: {} (expected 0)".format(result2))
print(__name__)