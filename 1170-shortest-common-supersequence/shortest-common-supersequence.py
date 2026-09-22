class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        i, j = m, n
        result = []        
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                result.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                result.append(str1[i - 1])
                i -= 1
            else:
                result.append(str2[j - 1])
                j -= 1
        while i > 0:
            result.append(str1[i - 1])
            i -= 1
        while j > 0:
            result.append(str2[j - 1])
            j -= 1
        result.reverse()        
        return "".join(result)
if __name__ == "__main__":
    solution = Solution()
    str1_1 = "abac"
    str2_1 = "cab"
    result1 = solution.shortestCommonSupersequence(str1_1, str2_1)
    print("Example 1: {} (length={})".format(result1, len(result1)))
    str1_2 = "aaaaaaaa"
    str2_2 = "aaaaaaaa"
    result2 = solution.shortestCommonSupersequence(str1_2, str2_2)
    print("Example 2: {} (Expected: aaaaaaaa)".format(result2))
print(__name__)