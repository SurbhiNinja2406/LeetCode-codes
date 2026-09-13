class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        stack = []
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        max_width = 0
        for j in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                i = stack.pop()
                max_width = max(max_width, j - i)        
        return max_width
if __name__ == "__main__":
    sol = Solution()
    nums1 = [6, 0, 8, 2, 1, 5]
    result1 = sol.maxWidthRamp(nums1)
    print("Input: {}".format(nums1))
    print("Output: {}".format(result1))
    print("Expected: 4")
    print("Pass: {}\n".format(result1 == 4))
    nums2 = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]
    result2 = sol.maxWidthRamp(nums2)
    print("Input: {}".format(nums2))
    print("Output: {}".format(result2))
    print("Expected: 7")
    print("Pass: {}\n".format(result2 == 7))
    nums3 = [5, 4, 3, 2, 1]
    result3 = sol.maxWidthRamp(nums3)
    print("Input: {}".format(nums3))
    print("Output: {}".format(result3))
    print("Expected: 0")
    print("Pass: {}\n".format(result3 == 0))
    nums4 = [1, 2, 3, 4, 5]
    result4 = sol.maxWidthRamp(nums4)
    print("Input: {}".format(nums4))
    print("Output: {}".format(result4))
    print("Expected: 4")
    print("Pass: {}\n".format(result4 == 4))
    nums5 = [3, 3, 3, 3]
    result5 = sol.maxWidthRamp(nums5)
    print("Input: {}".format(nums5))
    print("Output: {}".format(result5))
    print("Expected: 3")
    print("Pass: {}\n".format(result5 == 3))
    nums6 = [1, 5]
    result6 = sol.maxWidthRamp(nums6)
    print("Input: {}".format(nums6))
    print("Output: {}".format(result6))
    print("Expected: 1")
    print("Pass: {}\n".format(result6 == 1))
print(__name__)