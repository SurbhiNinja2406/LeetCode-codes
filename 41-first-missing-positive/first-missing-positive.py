class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 0]
    print(solution.firstMissingPositive(nums1)) 
    nums2 = [3, 4, -1, 1]
    print(solution.firstMissingPositive(nums2))  
    nums3 = [7, 8, 9, 11, 12]
    print(solution.firstMissingPositive(nums3)) 
print(__name__)