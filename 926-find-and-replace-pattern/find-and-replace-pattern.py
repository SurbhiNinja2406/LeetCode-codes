class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def matches(word, pattern):
            if len(word) != len(pattern):
                return False
            w_to_p = {}
            p_to_w = {}
            for w_char, p_char in zip(word, pattern):
                if w_char in w_to_p:
                    if w_to_p[w_char] != p_char:
                        return False
                else:
                    w_to_p[w_char] = p_char
                if p_char in p_to_w:
                    if p_to_w[p_char] != w_char:
                        return False
                else:
                    p_to_w[p_char] = w_char
            return True
        return [word for word in words if matches(word, pattern)]
if __name__ == "__main__":
    sol = Solution()
    words1 = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
    pattern1 = "abb"
    result1 = sol.findAndReplacePattern(words1, pattern1)
    print("Example 1: {} (expected ['mee', 'aqq'])".format(result1))
    words2 = ["a", "b", "c"]
    pattern2 = "a"
    result2 = sol.findAndReplacePattern(words2, pattern2)
    print("Example 2: {} (expected ['a', 'b', 'c'])".format(result2))
print(__name__)