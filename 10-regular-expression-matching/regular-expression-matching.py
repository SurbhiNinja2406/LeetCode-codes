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
                dp[0][j] = dp[0][j - 2]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    preceding_char = p[j - 2]
                    if preceding_char == '.' or preceding_char == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[m][n]
if __name__ == "__main__":
    sol = Solution()
    print(sol.isMatch("aa", "a")) 
    print(sol.isMatch("aa", "a*"))  
    print(sol.isMatch("ab", ".*"))  
    print(sol.isMatch("aa", "aa"))  
    print(sol.isMatch("aab", "c*a*b"))  
    print(sol.isMatch("a", "."))  
    print(sol.isMatch("mississippi", "mis*is*p*."))  
    print(sol.isMatch("aaa", "a*a"))  
    print(sol.isMatch("mississippi", "mis*is*ip*."))  