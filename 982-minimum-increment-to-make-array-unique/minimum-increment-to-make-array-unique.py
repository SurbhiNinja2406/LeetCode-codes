class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        moves = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                needed = nums[i - 1] + 1
                moves += needed - nums[i]
                nums[i] = needed
        return moves
if __name__ == "__main__":
    sol = Solution()
    print(sol.minIncrementForUnique([1, 2, 2]))  
    print(sol.minIncrementForUnique([3, 2, 1, 2, 1, 7])) 
print(__name__)