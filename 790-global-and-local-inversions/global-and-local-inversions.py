class Solution(object):
    def isIdealPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i, num in enumerate(nums):
            if abs(num - i) > 1:
                return False
        return True
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 0, 2]
    print("Input: nums = {}".format(nums))
    print("Output: {}".format(sol.isIdealPermutation(nums)))
    print("Expected: True\n")
    nums = [1, 2, 0]
    print("Input: nums = {}".format(nums))
    print("Output: {}".format(sol.isIdealPermutation(nums)))
    print("Expected: False\n")
print(__name__)