class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] % 2 == 0:
                left += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
        return nums
if __name__ == "__main__":
    solution = Solution()
    nums1 = [3, 1, 2, 4]
    print("Example 1:")
    print("Input: nums =", nums1)
    print("Output:", solution.sortArrayByParity(nums1[:]))
    print()
    nums2 = [0]
    print("Example 2:")
    print("Input: nums =", nums2)
    print("Output:", solution.sortArrayByParity(nums2[:]))
print(__name__)