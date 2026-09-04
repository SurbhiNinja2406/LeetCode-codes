class Solution(object):
    def bestRotation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        diff = [0] * (n + 1)
        for i in range(n):
            low = (i + 1) % n
            high = (i - nums[i]) % n
            if low <= high:
                diff[low] += 1
                diff[high + 1] -= 1
            else:
                diff[low] += 1
                diff[n] -= 1
                diff[0] += 1
                diff[high + 1] -= 1
        best_k = 0
        best_score = -1
        current_score = 0
        for k in range(n):
            current_score += diff[k]
            if current_score > best_score:
                best_score = current_score
                best_k = k
        return best_k
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([2, 3, 1, 4, 0], 3),
        ([1, 3, 0, 2, 4], 0),
        ([0], 0),
        ([1, 0], 0),
    ]
    for nums, expected in test_cases:
        result = solution.bestRotation(list(nums))
        status = "PASS" if result == expected else "FAIL"
        print("nums={:<20} expected={} got={} [{}]".format(
            repr(nums), expected, result, status))
print(__name__)