class Solution(object):
    def canTransform(self, start, result):
        """
        :type start: str
        :type result: str
        :rtype: bool
        """
        n, m = len(start), len(result)
        s_filtered = [(ch, i) for i, ch in enumerate(start) if ch != 'X']
        r_filtered = [(ch, i) for i, ch in enumerate(result) if ch != 'X']
        if len(s_filtered) != len(r_filtered):
            return False
        for (s_ch, s_idx), (r_ch, r_idx) in zip(s_filtered, r_filtered):
            if s_ch != r_ch:
                return False
            if s_ch == 'L' and s_idx < r_idx:
                return False
            if s_ch == 'R' and s_idx > r_idx:
                return False
        return True
if __name__ == "__main__":
    sol = Solution()
    start, result = "RXXLRXRXL", "XRLXXRRLX"
    print("Input: start = {}, result = {}".format(start, result))
    print("Output: {}".format(sol.canTransform(start, result)))
    print("Expected: True\n")
    start, result = "X", "L"
    print("Input: start = {}, result = {}".format(start, result))
    print("Output: {}".format(sol.canTransform(start, result)))
    print("Expected: False\n")
print(__name__)