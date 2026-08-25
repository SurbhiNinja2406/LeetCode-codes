class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0        
        jumps = 0
        current_end = 0     
        farthest = 0         
        for i in range(n - 1):  
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
                if current_end >= n - 1:
                    break        
        return jumps
if __name__ == "__main__":
    solution = Solution()
    nums1 = [2, 3, 1, 1, 4]
    print(solution.jump(nums1))  
    nums2 = [2, 3, 0, 1, 4]
    print(solution.jump(nums2)) 
print(__name__)