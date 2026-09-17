class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        result = []
        value = 0
        for bit in nums:
            value = (value * 2 + bit) % 5
            result.append(value == 0)
        return result
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([0, 1, 1], [True, False, False]),
        ([1, 1, 1], [False, False, False]),
        ([0, 0, 0, 0, 0], [True, True, True, True, True]),
        ([1, 0, 1, 0, 1, 0], [False, False, False, False, True, False]),
    ]
    for nums, expected in test_cases:
        result = sol.prefixesDivBy5(nums)
        status = "PASS" if result == expected else "FAIL"
        print("nums={0} -> {1} (expected {2}) [{3}]".format(
            nums, result, expected, status
        ))
print(__name__)