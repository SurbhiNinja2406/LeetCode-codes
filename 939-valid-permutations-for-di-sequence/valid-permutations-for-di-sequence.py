class Solution(object):
    def numPermsDISequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(s)
        dp = [1]
        for ch in s:
            new_len = len(dp) + 1
            new_dp = [0] * new_len
            if ch == 'I':
                prefix = 0
                for j in range(new_len):
                    if j - 1 < len(dp):
                        if j >= 1:
                            prefix += dp[j - 1]
                    new_dp[j] = prefix % MOD
            else:  
                suffix = sum(dp) % MOD
                for j in range(new_len):
                    new_dp[j] = suffix % MOD
                    if j < len(dp):
                        suffix -= dp[j]
            dp = new_dp
        return sum(dp) % MOD
if __name__ == "__main__":
    solution = Solution()
    s1 = "DID"
    print("Example 1:")
    print("Input: s =", repr(s1))
    print("Output:", solution.numPermsDISequence(s1))
    print()
    s2 = "D"
    print("Example 2:")
    print("Input: s =", repr(s2))
    print("Output:", solution.numPermsDISequence(s2))
print(__name__)