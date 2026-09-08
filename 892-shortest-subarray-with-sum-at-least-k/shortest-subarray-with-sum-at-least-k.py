from collections import deque

class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        dq = deque()
        ans = n + 1
        for j in range(n + 1):
            while dq and prefix[j] - prefix[dq[0]] >= k:
                ans = min(ans, j - dq.popleft())
            while dq and prefix[j] <= prefix[dq[-1]]:
                dq.pop()
            dq.append(j)
        return ans if ans <= n else -1
if __name__ == "__main__":
    sol = Solution()
    nums1, k1 = [1], 1
    result1 = sol.shortestSubarray(nums1, k1)
    print("Example 1:")
    print("Input: nums = {}, k = {}".format(nums1, k1))
    print("Output:", result1)
    print("Expected: 1")
    print()
    nums2, k2 = [1, 2], 4
    result2 = sol.shortestSubarray(nums2, k2)
    print("Example 2:")
    print("Input: nums = {}, k = {}".format(nums2, k2))
    print("Output:", result2)
    print("Expected: -1")
    print()
    nums3, k3 = [2, -1, 2], 3
    result3 = sol.shortestSubarray(nums3, k3)
    print("Example 3:")
    print("Input: nums = {}, k = {}".format(nums3, k3))
    print("Output:", result3)
    print("Expected: 3")
    print()
    nums4, k4 = [84, -37, 32, 40, 95], 167
    result4 = sol.shortestSubarray(nums4, k4)
    print("Additional test:")
    print("Input: nums = {}, k = {}".format(nums4, k4))
    print("Output:", result4)
    print("Expected: 3")
print(__name__)