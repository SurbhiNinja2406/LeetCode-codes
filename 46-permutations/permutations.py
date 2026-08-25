class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []        
        def backtrack(path, remaining):
            if not remaining:
                result.append(path[:])
                return            
            for i in range(len(remaining)):
                path.append(remaining[i])
                backtrack(path, remaining[:i] + remaining[i+1:])
                path.pop()        
        backtrack([], nums)
        return result
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 3]
    print(solution.permute(nums1))
    nums2 = [0, 1]
    print(solution.permute(nums2))
    nums3 = [1]
    print(solution.permute(nums3))
print(__name__)