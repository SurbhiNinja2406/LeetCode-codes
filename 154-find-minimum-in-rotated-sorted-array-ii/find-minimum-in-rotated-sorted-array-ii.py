class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]
if __name__ == "__main__":
    sol = Solution()
    print(sol.findMin([1, 3, 5]))       
    print(sol.findMin([2, 2, 2, 0, 1])) 
    print(sol.findMin([4, 5, 6, 7, 0, 1, 4])) 
print(__name__)