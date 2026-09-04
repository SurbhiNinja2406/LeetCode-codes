class Solution(object):
    def expressiveWords(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        def get_groups(string):
            groups = []
            i = 0
            n = len(string)
            while i < n:
                j = i
                while j < n and string[j] == string[i]:
                    j += 1
                groups.append((string[i], j - i))
                i = j
            return groups
        def is_stretchy(word_groups, s_groups):
            if len(word_groups) != len(s_groups):
                return False
            for (char_w, count_w), (char_s, count_s) in zip(word_groups, s_groups):
                if char_w != char_s:
                    return False
                if count_w == count_s:
                    continue
                if count_w < count_s and count_s >= 3:
                    continue
                return False
            return True
        s_groups = get_groups(s)
        result = 0
        for word in words:
            word_groups = get_groups(word)
            if is_stretchy(word_groups, s_groups):
                result += 1
        return result
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("heeellooo", ["hello", "hi", "helo"], 1),
        ("zzzzzyyyyy", ["zzyy", "zy", "zyy"], 3),
    ]
    for s, words, expected in test_cases:
        result = solution.expressiveWords(s, list(words))
        status = "PASS" if result == expected else "FAIL"
        print("s={:<15} words={:<25} expected={} got={} [{}]".format(
            s, str(words), expected, result, status))
print(__name__)