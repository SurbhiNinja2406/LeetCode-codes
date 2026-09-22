class Solution(object):
    def canDivideIntoSubsequences(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        max_freq = 1
        current_freq = 1        
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                current_freq += 1
            else:
                current_freq = 1
            max_freq = max(max_freq, current_freq)
        num_subsequences = max_freq
        max_min_length = n // num_subsequences        
        return max_min_length >= k
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 2, 3, 3, 4, 4]
    k1 = 3
    result1 = solution.canDivideIntoSubsequences(nums1, k1)
    print("Example 1: {} (Expected: True)".format(result1))
    nums2 = [5, 6, 6, 7, 8]
    k2 = 3
    result2 = solution.canDivideIntoSubsequences(nums2, k2)
    print("Example 2: {} (Expected: False)".format(result2))
print(__name__)