class Solution(object):
    def numSpecialEquivGroups(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        signatures = set()
        for word in words:
            even_chars = sorted(word[0::2])
            odd_chars = sorted(word[1::2])
            signature = (tuple(even_chars), tuple(odd_chars))
            signatures.add(signature)
        return len(signatures)
if __name__ == "__main__":
    sol = Solution()
    words1 = ["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"]
    result1 = sol.numSpecialEquivGroups(words1)
    print("Example 1: {} (expected 3)".format(result1))
    words2 = ["abc", "acb", "bac", "bca", "cab", "cba"]
    result2 = sol.numSpecialEquivGroups(words2)
    print("Example 2: {} (expected 3)".format(result2))
print(__name__)