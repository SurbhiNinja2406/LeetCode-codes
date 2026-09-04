class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        word_set = set(words)
        for word in words:
            for i in range(1, len(word)):
                suffix = word[i:]
                word_set.discard(suffix)
        return sum(len(word) + 1 for word in word_set)
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (["time", "me", "bell"], 10),
        (["t"], 2),
    ]
    for words, expected in test_cases:
        result = solution.minimumLengthEncoding(list(words))
        status = "PASS" if result == expected else "FAIL"
        print("words={:<25} expected={} got={} [{}]".format(
            str(words), expected, result, status))
print(__name__)