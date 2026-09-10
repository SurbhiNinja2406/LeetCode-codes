class Solution(object):
    def smallestRangeII(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        ans = nums[-1] - nums[0]
        for i in range(n - 1):
            high = max(nums[i] + k, nums[-1] - k)
            low = min(nums[0] + k, nums[i + 1] - k)
            ans = min(ans, high - low)
        return ans
if __name__ == "__main__":
    solution = Solution()
    nums1, k1 = [1], 0
    print("Example 1:")
    print("Input: nums =", nums1, ", k =", k1)
    print("Output:", solution.smallestRangeII(nums1[:], k1))
    print()
    nums2, k2 = [0, 10], 2
    print("Example 2:")
    print("Input: nums =", nums2, ", k =", k2)
    print("Output:", solution.smallestRangeII(nums2[:], k2))
    print()
    nums3, k3 = [1, 3, 6], 3
    print("Example 3:")
    print("Input: nums =", nums3, ", k =", k3)
    print("Output:", solution.smallestRangeII(nums3[:], k3))
print(__name__)