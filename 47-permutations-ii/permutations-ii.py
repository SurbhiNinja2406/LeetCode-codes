class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()  
        used = [False] * len(nums)        
        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])
                return            
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(nums[i])                
                backtrack(path)                
                path.pop()
                used[i] = False        
        backtrack([])
        return result
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 1, 2]
    print(solution.permuteUnique(nums1))
    nums2 = [1, 2, 3]
    print(solution.permuteUnique(nums2))
print(__name__)