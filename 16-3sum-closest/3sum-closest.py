class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2] 
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                if current_sum == target:
                    return current_sum
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        return closest_sum
if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSumClosest([-1, 2, 1, -4], 1)) 
    print(sol.threeSumClosest([0, 0, 0], 1)) 
    print(sol.threeSumClosest([1, 1, 1, 0], -100)) 
    print(sol.threeSumClosest([1, 2, 4, 8, 16], 15))  
    print(sol.threeSumClosest([-5, -4, -3, -2, -1], -10)) 
    print(sol.threeSumClosest([1, 1, 1, 1], 0))  
print(__name__)