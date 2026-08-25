class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  
        dp[1] = 1  
        for i in range(2, n + 1):
            one_digit = int(s[i - 1])
            two_digit = int(s[i - 2:i])
            if one_digit >= 1:  
                dp[i] += dp[i - 1]
            if 10 <= two_digit <= 26:  
                dp[i] += dp[i - 2]
        return dp[n]
if __name__ == "__main__":
    sol = Solution()
    print(sol.numDecodings("12"))  
    print(sol.numDecodings("226")) 
    print(sol.numDecodings("06"))  
print(__name__)