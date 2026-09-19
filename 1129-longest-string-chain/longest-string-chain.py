class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dp = {}
        best = 1
        for word in sorted(words, key=len):
            cur = 1
            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]   
                if prev in dp:
                    cur = max(cur, dp[prev] + 1)
            dp[word] = cur
            best = max(best, cur)
        return best
if __name__ == "__main__":
    sol = Solution()
    tests = [
        (["a", "b", "ba", "bca", "bda", "bdca"], 4),
        (["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"], 5),
        (["abcd", "dbqca"], 1),
        (["a"], 1),
    ]
    for words, expected in tests:
        result = sol.longestStrChain(words)
        status = "PASS" if result == expected else "FAIL"
        print("{}: got {}, expected {}".format(status, result, expected))
print(__name__)