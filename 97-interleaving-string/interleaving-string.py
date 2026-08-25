class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                k = i + j - 1  
                take_from_s1 = dp[i - 1][j] and s1[i - 1] == s3[k]
                take_from_s2 = dp[i][j - 1] and s2[j - 1] == s3[k]
                dp[i][j] = take_from_s1 or take_from_s2
        return dp[m][n]
if __name__ == "__main__":
    sol = Solution()
    print("Test 1: {}".format(sol.isInterleave("aabcc", "dbbca", "aadbbcbcac")))  
    print("Test 2: {}".format(sol.isInterleave("aabcc", "dbbca", "aadbbbaccc"))) 
    print("Test 3: {}".format(sol.isInterleave("", "", "")))  
print(__name__)