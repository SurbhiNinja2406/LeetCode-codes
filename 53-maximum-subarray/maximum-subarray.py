class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        current_sum = nums[0]        
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)        
        return max_sum
if __name__ == "__main__":
    solution = Solution()
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(solution.maxSubArray(nums1))  
    nums2 = [1]
    print(solution.maxSubArray(nums2))  
    nums3 = [5, 4, -1, 7, 8]
    print(solution.maxSubArray(nums3)) 
print(__name__)