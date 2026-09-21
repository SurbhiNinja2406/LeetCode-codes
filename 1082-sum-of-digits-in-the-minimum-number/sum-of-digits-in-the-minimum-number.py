class Solution(object):
    def sumOfDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest = min(nums)
        digit_sum = 0
        while smallest > 0:
            digit_sum += smallest % 10
            smallest //= 10
        return 1 - digit_sum % 2
if __name__ == "__main__":
    sol = Solution()
    tests = [
        [34, 23, 1, 24, 75, 33, 54, 8],  
        [99, 77, 33, 66, 55],       
    ]
    for t in tests:
        print("nums = {} -> {}".format(t, sol.sumOfDigits(t)))
print(__name__)