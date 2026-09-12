class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = 0
        last = {}
        for c in s:
            new_dp = (2 * dp + 1) % MOD
            if c in last:
                new_dp = (new_dp - last[c]) % MOD
            last[c] = (dp + 1) % MOD 
            dp = new_dp
        return dp % MOD
if __name__ == "__main__":
    sol = Solution()
    print(sol.distinctSubseqII("abc"))  
    print(sol.distinctSubseqII("aba"))  
    print(sol.distinctSubseqII("aaa")) 
print(__name__)