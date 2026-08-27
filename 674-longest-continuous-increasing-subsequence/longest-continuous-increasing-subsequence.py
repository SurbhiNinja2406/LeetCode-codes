class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_len = 1     
        cur_len = 1     
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur_len += 1
            else:
                cur_len = 1
            max_len = max(max_len, cur_len)
        return max_len
if __name__ == "__main__":
    solution = Solution()
    result1 = solution.findLengthOfLCIS([1, 3, 5, 4, 7])
    print("Example 1:")
    print("Input:  nums = [1,3,5,4,7]")
    print("Output:", result1)
    print("Expected: 3")
    print()
    result2 = solution.findLengthOfLCIS([2, 2, 2, 2, 2])
    print("Example 2:")
    print("Input:  nums = [2,2,2,2,2]")
    print("Output:", result2)
    print("Expected: 1")
    print()
    result3 = solution.findLengthOfLCIS([9])
    print("Example 3 (extra):")
    print("Input:  nums = [9]")
    print("Output:", result3)
    print("Expected: 1")
    print()
    result4 = solution.findLengthOfLCIS([1, 2, 3, 4, 5])
    print("Example 4 (extra):")
    print("Input:  nums = [1,2,3,4,5]")
    print("Output:", result4)
    print("Expected: 5")
    print()

    # Strictly decreasing entire array
    result5 = solution.findLengthOfLCIS([5, 4, 3, 2, 1])
    print("Example 5 (extra):")
    print("Input:  nums = [5,4,3,2,1]")
    print("Output:", result5)
    print("Expected: 1")
    print()

    # Multiple runs, longest in the middle
    result6 = solution.findLengthOfLCIS([1, 3, 5, 7, 2, 3, 4, 1, 2])
    print("Example 6 (extra):")
    print("Input:  nums = [1,3,5,7,2,3,4,1,2]")
    print("Output:", result6)
    print("Expected: 4")
print(__name__)