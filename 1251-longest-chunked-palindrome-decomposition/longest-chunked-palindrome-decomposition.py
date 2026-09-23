class Solution(object):
    def longestDecomposition(self, text):
        """
        :type text: str
        :rtype: int
        """
        n = len(text)
        res = 0
        left, right = "", ""
        for i in range(n):
            left += text[i]
            right = text[n - 1 - i] + right
            if left == right:
                res += 1
                left, right = "", ""
        return res
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("ghiabcdefhelloadamhelloabcdefghi", 7),
        ("merchant", 1),
        ("antaprezatepzapreanta", 11),
        ("aaa", 3),
        ("a", 1),
    ]
    for text, expected in tests:
        result = sol.longestDecomposition(text)
        status = "PASS" if result == expected else "FAIL"
        print("%s | input: %r | output: %d | expected: %d" % (status, text, result, expected))
print(__name__)