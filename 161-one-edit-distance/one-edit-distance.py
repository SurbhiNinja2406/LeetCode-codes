class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_s, len_t = len(s), len(t)
        if len_s > len_t:
            return self.isOneEditDistance(t, s)
        if len_t - len_s > 1:
            return False        
        for i in range(len_s):
            if s[i] != t[i]:
                if len_s == len_t:
                    return s[i+1:] == t[i+1:]
                else:
                    return s[i:] == t[i+1:]
        return len_s + 1 == len_t
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("ab", "acb", True),
        ("", "", False),
        ("cab", "ad", False),
        ("1203", "1213", True),
        ("", "a", True),
        ("a", "", True),
        ("abc", "abc", False),
        ("abcd", "abd", True),
        ("abc", "abcd", True),
        ("ab", "ba", False),
    ]
    for s, t, expected in test_cases:
        result = solution.isOneEditDistance(s, t)
        status = "PASS" if result == expected else "FAIL"
        print("[{0}] s={1!r}, t={2!r} -> got {3}, expected {4}".format(
            status, s, t, result, expected
        ))
print(__name__)