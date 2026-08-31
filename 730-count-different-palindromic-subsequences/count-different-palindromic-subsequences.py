class Solution(object):
    def countPalindromicSubsequences(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(s)
        if n == 0:
            return 0
        chars = ['a', 'b', 'c', 'd']
        char_to_idx = {c: i for i, c in enumerate(chars)}
        s_idx = [char_to_idx[c] for c in s]
        next_occ = [[n] * 4 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for c in range(4):
                if s_idx[i] == c:
                    next_occ[i][c] = i
                else:
                    next_occ[i][c] = next_occ[i + 1][c]
        prev_occ = [[-1] * 4 for _ in range(n + 1)]
        for i in range(n):
            for c in range(4):
                if s_idx[i] == c:
                    prev_occ[i + 1][c] = i
                else:
                    prev_occ[i + 1][c] = prev_occ[i][c]
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1  
        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                ci, cj = s_idx[i], s_idx[j]

                if ci != cj:
                    dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % MOD
                else:
                    c = ci
                    low = next_occ[i + 1][c]
                    high = prev_occ[j][c]  
                    if low > j - 1:
                        inner = dp[i + 1][j - 1] if i + 1 <= j - 1 else 0
                        dp[i][j] = (2 * inner + 2) % MOD
                    elif low == high:
                        inner = dp[i + 1][j - 1] if i + 1 <= j - 1 else 0
                        dp[i][j] = (2 * inner + 1) % MOD
                    else:
                        outer = dp[i + 1][j - 1] if i + 1 <= j - 1 else 0
                        inner2 = dp[low + 1][high - 1] if low + 1 <= high - 1 else 0
                        dp[i][j] = (2 * outer - inner2) % MOD
        return dp[0][n - 1] % MOD
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("bccb", 6),
        ("abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba", 104860361),
        ("a", 1),
        ("aa", 2),
        ("aaa", 3),
        ("aba", 4), 
    ]
    for idx, (s, expected) in enumerate(test_cases, 1):
        result = solution.countPalindromicSubsequences(s)
        status = "PASS" if result == expected else "FAIL"
        print("Test %d: [%s]" % (idx, status))
        print("  Input:    s = \"%s...\"" % (s[:20] + ("..." if len(s) > 20 else "")))
        print("  Output:   %d" % result)
        print("  Expected: %d" % expected)
        print("")
print(__name__)