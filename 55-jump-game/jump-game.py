class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        farthest = 0
        for i in range(n):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            if farthest >= n - 1:
                return True        
        return True
if __name__ == "__main__":
    solution = Solution()
    nums1 = [2, 3, 1, 1, 4]
    print(solution.canJump(nums1)) 
    nums2 = [3, 2, 1, 0, 4]
    print(solution.canJump(nums2)) 
print(__name__)