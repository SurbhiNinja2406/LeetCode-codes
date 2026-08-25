class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = False        
        return dp[m][n]
if __name__ == "__main__":
    solution = Solution()
    s1, p1 = "aa", "a"
    print(solution.isMatch(s1, p1))  
    s2, p2 = "aa", "*"
    print(solution.isMatch(s2, p2))  
    s3, p3 = "cb", "?a"
    print(solution.isMatch(s3, p3)) 
print(__name__) 