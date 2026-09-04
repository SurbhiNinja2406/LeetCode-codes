class Solution(object):
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        def best_digit(value):
            best_x = 0
            best_diff = float('inf')
            for x in range(16):
                diff = abs(value - 17 * x)
                if diff < best_diff:
                    best_diff = diff
                    best_x = x
            return best_x
        def channel_value(hex_pair):
            return int(hex_pair, 16)
        r = channel_value(color[1:3])
        g = channel_value(color[3:5])
        b = channel_value(color[5:7])
        r_digit = best_digit(r)
        g_digit = best_digit(g)
        b_digit = best_digit(b)
        hex_chars = "0123456789abcdef"
        r_hex = hex_chars[r_digit]
        g_hex = hex_chars[g_digit]
        b_hex = hex_chars[b_digit]
        return "#{0}{0}{1}{1}{2}{2}".format(r_hex, g_hex, b_hex)
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("#09f166", "#11ee66"),
        ("#4e3fe1", "#5544dd"),
    ]
    for color, expected in test_cases:
        result = solution.similarRGB(color)
        status = "PASS" if result == expected else "FAIL"
        print("color={:<10} expected={:<10} got={:<10} [{}]".format(
            color, expected, result, status))
print(__name__)