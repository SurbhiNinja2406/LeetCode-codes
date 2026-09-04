class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        MAX_WIDTH = 100
        lines = 1
        current_width = 0
        for ch in s:
            char_width = widths[ord(ch) - ord('a')]
            if current_width + char_width > MAX_WIDTH:
                lines += 1
                current_width = char_width
            else:
                current_width += char_width
        return [lines, current_width]
if __name__ == "__main__":
    solution = Solution()
    widths1 = [10] * 26
    widths2 = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
               10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    test_cases = [
        (widths1, "abcdefghijklmnopqrstuvwxyz", [3, 60]),
        (widths2, "bbbcccdddaaa", [2, 4]),
    ]
    for widths, s, expected in test_cases:
        result = solution.numberOfLines(list(widths), s)
        status = "PASS" if result == expected else "FAIL"
        print("s={:<30} expected={:<10} got={:<10} [{}]".format(
            s, str(expected), str(result), status))
print(__name__)