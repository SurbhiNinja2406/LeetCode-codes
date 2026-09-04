class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]
        transformations = set()
        for word in words:
            code = "".join(morse[ord(ch) - ord('a')] for ch in word)
            transformations.add(code)
        return len(transformations)
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (["gin", "zen", "gig", "msg"], 2),
        (["a"], 1),
    ]
    for words, expected in test_cases:
        result = solution.uniqueMorseRepresentations(list(words))
        status = "PASS" if result == expected else "FAIL"
        print("words={:<28} expected={} got={} [{}]".format(
            str(words), expected, result, status))
print(__name__)