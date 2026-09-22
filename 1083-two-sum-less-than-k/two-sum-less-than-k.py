class Solution(object):
    def twoSumLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()        
        left, right = 0, len(nums) - 1
        max_sum = -1        
        while left < right:
            current_sum = nums[left] + nums[right]            
            if current_sum < k:
                max_sum = max(max_sum, current_sum)
                left += 1
            else:
                right -= 1        
        return max_sum
if __name__ == "__main__":
    solution = Solution()
    nums1 = [34, 23, 1, 24, 75, 33, 54, 8]
    k1 = 60
    result1 = solution.twoSumLessThanK(nums1, k1)
    print("Example 1: {} (Expected: 58)".format(result1))
    nums2 = [10, 20, 30]
    k2 = 15
    result2 = solution.twoSumLessThanK(nums2, k2)
    print("Example 2: {} (Expected: -1)".format(result2))
print(__name__)