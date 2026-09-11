class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        def atMost(target):
            if target < 0:
                return 0
            count = 0
            left = 0
            window_sum = 0
            for right in range(len(nums)):
                window_sum += nums[right]
                while window_sum > target:
                    window_sum -= nums[left]
                    left += 1
                count += right - left + 1
            return count
        return atMost(goal) - atMost(goal - 1)
if __name__ == "__main__":
    sol = Solution()
    print(sol.numSubarraysWithSum([1, 0, 1, 0, 1], 2))
    print(sol.numSubarraysWithSum([0, 0, 0, 0, 0], 0))
print(__name__)