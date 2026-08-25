class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0        
        for num in nums:
            result ^= num        
        return result
if __name__ == "__main__":
    sol = Solution()
    nums1 = [2, 2, 1]
    print(sol.singleNumber(nums1)) 
    nums2 = [4, 1, 2, 1, 2]
    print(sol.singleNumber(nums2))  
    nums3 = [1]
    print(sol.singleNumber(nums3)) 
print(__name__)