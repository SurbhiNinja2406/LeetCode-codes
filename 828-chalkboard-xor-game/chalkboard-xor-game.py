class Solution(object):
    def xorGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total_xor = 0
        for num in nums:
            total_xor ^= num
        n = len(nums)
        return total_xor == 0 or n % 2 == 0
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1, 1, 2], False),
        ([0, 1], True),
        ([1, 2, 3], True),
    ]
    for nums, expected in test_cases:
        result = solution.xorGame(list(nums))
        status = "PASS" if result == expected else "FAIL"
        print("nums={:<15} expected={} got={} [{}]".format(
            str(nums), expected, result, status))
print(__name__)