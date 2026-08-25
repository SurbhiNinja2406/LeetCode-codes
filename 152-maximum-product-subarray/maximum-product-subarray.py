class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            if num < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(num, cur_max * num)
            cur_min = min(num, cur_min * num)
            max_so_far = max(max_so_far, cur_max)
        return max_so_far
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct([2, 3, -2, 4])) 
    print(sol.maxProduct([-2, 0, -1]))  
    print(sol.maxProduct([-2, 3, -4]))  
print(__name__)