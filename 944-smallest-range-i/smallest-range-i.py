class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return max(0, (max(nums) - min(nums)) - 2 * k)
if __name__ == "__main__":
    solution = Solution()
    nums1, k1 = [1], 0
    print("Example 1:")
    print("Input: nums =", nums1, ", k =", k1)
    print("Output:", solution.smallestRangeI(nums1, k1))
    print()
    nums2, k2 = [0, 10], 2
    print("Example 2:")
    print("Input: nums =", nums2, ", k =", k2)
    print("Output:", solution.smallestRangeI(nums2, k2))
    print()
    nums3, k3 = [1, 3, 6], 3
    print("Example 3:")
    print("Input: nums =", nums3, ", k =", k3)
    print("Output:", solution.smallestRangeI(nums3, k3))
print(__name__)