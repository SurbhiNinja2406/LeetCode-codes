class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_len = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_len = max(max_len, dp[i][j])
        return max_len
if __name__ == "__main__":
    sol = Solution()
    print(sol.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
    print("Expected: 3\n")
    print(sol.findLength([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]))
    print("Expected: 5\n")
    print(sol.findLength([1, 2, 3], [4, 5, 6]))
    print("Expected: 0\n")
    print(sol.findLength([1, 2, 3], [7, 2, 8]))
    print("Expected: 1\n")
    print(sol.findLength([1, 2, 3, 4], [1, 2, 3, 4]))
    print("Expected: 4\n")
    print(sol.findLength([1, 4, 5, 2, 3], [7, 2, 3, 9]))
    print("Expected: 2")  
print(__name__)