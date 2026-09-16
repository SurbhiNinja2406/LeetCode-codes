class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]
            if b + c > a:
                return a + b + c
        return 0
if __name__ == "__main__":
    sol = Solution()
    print(sol.largestPerimeter([2, 1, 2]))   
    print(sol.largestPerimeter([1, 2, 1, 10])) 
print(__name__)