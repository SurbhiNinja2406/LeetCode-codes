class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = list(triangle[n - 1])
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        return dp[0]
if __name__ == "__main__":
    sol = Solution()
    print("Test 1: {}".format(sol.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))) 
    print("Test 2: {}".format(sol.minimumTotal([[-10]]))) 
print(__name__)