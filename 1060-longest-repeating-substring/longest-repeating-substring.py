class Solution(object):
    def longestRepeatingSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        best = 0
        prev = [0] * (n + 1)
        for i in range(1, n + 1):
            cur = [0] * (n + 1)
            for j in range(i + 1, n + 1):
                if s[i - 1] == s[j - 1]:
                    cur[j] = prev[j - 1] + 1
                    if cur[j] > best:
                        best = cur[j]
            prev = cur
        return best
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestRepeatingSubstring("abcd"))   
    print(sol.longestRepeatingSubstring("abbaba")) 
    print(sol.longestRepeatingSubstring("aabcaabdaab")) 
    print(sol.longestRepeatingSubstring("aaaa"))      
print(__name__)