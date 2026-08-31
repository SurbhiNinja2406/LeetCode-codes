class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_val = max(nums)
        points = [0] * (max_val + 1)
        for num in nums:
            points[num] += num
        take = 0   
        skip = 0   
        for i in range(len(points)):
            new_take = skip + points[i]
            new_skip = max(take, skip)
            take, skip = new_take, new_skip
        return max(take, skip)
if __name__ == "__main__":
    sol = Solution()
    print(sol.deleteAndEarn([3, 4, 2]))
    print(sol.deleteAndEarn([2, 2, 3, 3, 3, 4]))
print(__name__)