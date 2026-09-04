class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned_set = set(word.lower() for word in banned)
        cleaned = []
        for ch in paragraph.lower():
            if ch.isalpha():
                cleaned.append(ch)
            else:
                cleaned.append(' ')
        words = "".join(cleaned).split()
        counts = {}
        for word in words:
            if word in banned_set:
                continue
            counts[word] = counts.get(word, 0) + 1
        best_word = None
        best_count = 0
        for word, count in counts.items():
            if count > best_count:
                best_count = count
                best_word = word
        return best_word
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"], "ball"),
        ("a.", [], "a"),
    ]
    for paragraph, banned, expected in test_cases:
        result = solution.mostCommonWord(paragraph, list(banned))
        status = "PASS" if result == expected else "FAIL"
        print("paragraph={!r:60} banned={:<12} expected={!r} got={!r} [{}]".format(
            paragraph, str(banned), expected, result, status))
print(__name__)