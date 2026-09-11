class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        cur_max, max_sum = 0, nums[0]
        cur_min, min_sum = 0, nums[0]
        for num in nums:
            total += num
            cur_max = max(cur_max + num, num)
            max_sum = max(max_sum, cur_max)
            cur_min = min(cur_min + num, num)
            min_sum = min(min_sum, cur_min)
        if max_sum < 0:
            return max_sum
        return max(max_sum, total - min_sum)
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubarraySumCircular([1, -2, 3, -2]))
    print(sol.maxSubarraySumCircular([5, -3, 5]))
    print(sol.maxSubarraySumCircular([-3, -2, -3]))
print(__name__)