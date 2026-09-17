class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atMostKDistinct(nums, k):
            if k == 0:
                return 0
            count = {}
            left = 0
            result = 0
            for right in range(len(nums)):
                count[nums[right]] = count.get(nums[right], 0) + 1
                while len(count) > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1
                result += right - left + 1
            return result
        return atMostKDistinct(nums, k) - atMostKDistinct(nums, k - 1)
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([1, 2, 1, 2, 3], 2, 7),
        ([1, 2, 1, 3, 4], 3, 3),
        ([1, 2, 1, 2, 3], 3, 3),
        ([1, 1, 1, 1], 1, 10),
        ([1, 2, 3], 1, 3),
    ]
    for nums, k, expected in test_cases:
        result = sol.subarraysWithKDistinct(nums, k)
        status = "PASS" if result == expected else "FAIL"
        print("nums={0}, k={1} -> {2} (expected {3}) [{4}]".format(
            nums, k, result, expected, status
        ))
print(__name__)