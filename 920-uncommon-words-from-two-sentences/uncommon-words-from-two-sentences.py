from collections import Counter
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        word_count = Counter((s1 + " " + s2).split())
        return [word for word, count in word_count.items() if count == 1]
if __name__ == "__main__":
    sol = Solution()
    s1_1, s2_1 = "this apple is sweet", "this apple is sour"
    result1 = sol.uncommonFromSentences(s1_1, s2_1)
    print("Example 1: {} (expected [sweet, sour] in any order)".format(result1))
    s1_2, s2_2 = "apple apple", "banana"
    result2 = sol.uncommonFromSentences(s1_2, s2_2)
    print("Example 2: {} (expected [banana])".format(result2))
print(__name__)