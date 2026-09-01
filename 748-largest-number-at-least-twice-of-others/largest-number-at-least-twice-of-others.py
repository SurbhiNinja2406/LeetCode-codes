class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_index = 0
        for i in range(len(nums)):
            if nums[i] > nums[max_index]:
                max_index = i
        for i in range(len(nums)):
            if i != max_index and nums[i] * 2 > nums[max_index]:
                return -1
        return max_index
if __name__ == "__main__":
    solution = Solution()
    nums1 = [3, 6, 1, 0]
    result1 = solution.dominantIndex(nums1)
    print("Example 1: Output = {0}, Expected = 1".format(result1))
    assert result1 == 1
    nums2 = [1, 2, 3, 4]
    result2 = solution.dominantIndex(nums2)
    print("Example 2: Output = {0}, Expected = -1".format(result2))
    assert result2 == -1
    print("\nAll test cases passed!")
print(__name__)