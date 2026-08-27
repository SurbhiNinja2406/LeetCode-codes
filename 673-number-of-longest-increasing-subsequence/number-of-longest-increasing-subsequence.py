class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        length = [1] * n
        count = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]
        max_length = max(length)
        return sum(c for l, c in zip(length, count) if l == max_length)
if __name__ == "__main__":
    solution = Solution()
    result1 = solution.findNumberOfLIS([1, 3, 5, 4, 7])
    print("Example 1:")
    print("Input:  nums = [1,3,5,4,7]")
    print("Output:", result1)
    print("Expected: 2")
    print()
    result2 = solution.findNumberOfLIS([2, 2, 2, 2, 2])
    print("Example 2:")
    print("Input:  nums = [2,2,2,2,2]")
    print("Output:", result2)
    print("Expected: 5")
    print()
    result3 = solution.findNumberOfLIS([7])
    print("Example 3 (extra):")
    print("Input:  nums = [7]")
    print("Output:", result3)
    print("Expected: 1")
    print()
    result4 = solution.findNumberOfLIS([1, 2, 3, 4])
    print("Example 4 (extra):")
    print("Input:  nums = [1,2,3,4]")
    print("Output:", result4)
    print("Expected: 1")
    print()
    result5 = solution.findNumberOfLIS([1, 3, 5, 4, 7, 2])
    print("Example 5 (extra):")
    print("Input:  nums = [1,3,5,4,7,2]")
    print("Output:", result5)
    print("Expected: 2") 
print(__name__)