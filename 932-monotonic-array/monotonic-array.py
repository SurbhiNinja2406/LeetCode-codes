class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        is_increasing = True
        is_decreasing = True
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                is_decreasing = False
            if nums[i] < nums[i - 1]:
                is_increasing = False
        return is_increasing or is_decreasing
if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 2, 2, 3]
    result1 = sol.isMonotonic(nums1)
    print("Example 1: {} (expected True)".format(result1))
    nums2 = [6, 5, 4, 4]
    result2 = sol.isMonotonic(nums2)
    print("Example 2: {} (expected True)".format(result2))
    nums3 = [1, 3, 2]
    result3 = sol.isMonotonic(nums3)
    print("Example 3: {} (expected False)".format(result3))