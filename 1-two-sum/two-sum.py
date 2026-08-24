class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}  
        for i, num in enumerate(nums):
            complement = target - num            
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
if __name__ == "__main__":
    sol = Solution()
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(sol.twoSum(nums1, target1))  
    nums2 = [3, 2, 4]
    target2 = 6
    print(sol.twoSum(nums2, target2)) 
    nums3 = [3, 3]
    target3 = 6
    print(sol.twoSum(nums3, target3))  
print(__name__)