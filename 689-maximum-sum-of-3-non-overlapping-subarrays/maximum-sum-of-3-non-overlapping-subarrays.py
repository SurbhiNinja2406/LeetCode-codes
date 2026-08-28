class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        num_windows = n - k + 1
        window_sum = [0] * num_windows
        curr = sum(nums[:k])
        window_sum[0] = curr
        for i in range(1, num_windows):
            curr += nums[i + k - 1] - nums[i - 1]
            window_sum[i] = curr
        left = [0] * num_windows
        best = 0
        for i in range(num_windows):
            if window_sum[i] > window_sum[best]:
                best = i
            left[i] = best
        right = [0] * num_windows
        best = num_windows - 1
        for i in range(num_windows - 1, -1, -1):
            if window_sum[i] >= window_sum[best]:
                best = i
            right[i] = best
        max_total = -1
        result = []
        for j in range(k, num_windows - k):
            l = left[j - k]
            r = right[j + k]
            total = window_sum[l] + window_sum[j] + window_sum[r]
            if total > max_total:
                max_total = total
                result = [l, j, r]
        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2)) 
    print(sol.maxSumOfThreeSubarrays([1,2,1,2,1,2,1,2,1], 2)) 
print(__name__)