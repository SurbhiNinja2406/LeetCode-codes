class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort() 
        result = []
        subset = []
        def backtrack(start):
            result.append(subset[:]) 
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()
        backtrack(0)
        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.subsetsWithDup([1, 2, 2]))
    print(sol.subsetsWithDup([0]))
print(__name__)