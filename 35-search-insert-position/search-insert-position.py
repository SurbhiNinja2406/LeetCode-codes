class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1        
        return left
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 3, 5, 6]
    target1 = 5
    print(solution.searchInsert(nums1, target1))  
    nums2 = [1, 3, 5, 6]
    target2 = 2
    print(solution.searchInsert(nums2, target2)) 
    nums3 = [1, 3, 5, 6]
    target3 = 7
    print(solution.searchInsert(nums3, target3))  
print(__name__)