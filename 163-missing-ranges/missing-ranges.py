class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[List[int]]
        """
        result = []
        prev = lower - 1
        for i in range(len(nums) + 1):
            curr = nums[i] if i < len(nums) else upper + 1
            if curr - prev >= 2:
                result.append([prev + 1, curr - 1])            
            prev = curr        
        return result
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([0, 1, 3, 50, 75], 0, 99, [[2, 2], [4, 49], [51, 74], [76, 99]]),
        ([-1], -1, -1, []),
        ([], 1, 1, [[1, 1]]),
        ([], 5, 10, [[5, 10]]),
        ([-5], -5, -5, []),
        ([2, 3, 6, 7], 1, 10, [[1, 1], [4, 5], [8, 10]]),
        ([10], 1, 10, [[1, 9]]),
        ([1], 1, 10, [[2, 10]]),
    ]
    for nums, lower, upper, expected in test_cases:
        result = solution.findMissingRanges(nums, lower, upper)
        status = "PASS" if result == expected else "FAIL"
        print("[{0}] nums={1}, lower={2}, upper={3} -> got {4}, expected {5}".format(
            status, nums, lower, upper, result, expected
        ))
print(__name__)