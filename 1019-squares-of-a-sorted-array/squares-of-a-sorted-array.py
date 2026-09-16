class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        for pos in range(n - 1, -1, -1):
            left_val = nums[left] * nums[left]
            right_val = nums[right] * nums[right]
            if left_val > right_val:
                result[pos] = left_val
                left += 1
            else:
                result[pos] = right_val
                right -= 1
        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.sortedSquares([-4, -1, 0, 3, 10]))  
    print(sol.sortedSquares([-7, -3, 2, 3, 11])) 
print(__name__)