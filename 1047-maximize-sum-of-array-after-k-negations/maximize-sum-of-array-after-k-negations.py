class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        i = 0
        n = len(nums)
        while i < n and nums[i] < 0 and k > 0:
            nums[i] = -nums[i]
            k -= 1
            i += 1
        total = sum(nums)
        if k % 2 == 1:
            min_val = min(nums)
            total -= 2 * min_val
        return total
if __name__ == "__main__":
    sol = Solution()
    print(sol.largestSumAfterKNegations([4, 2, 3], 1))  
    print(sol.largestSumAfterKNegations([3, -1, 0, 2], 3)) 
    print(sol.largestSumAfterKNegations([2, -3, -1, 5, -4], 2))  
print(__name__)