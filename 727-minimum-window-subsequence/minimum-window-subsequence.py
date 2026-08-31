class Solution(object):
    def minWindow(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: str
        """
        n, m = len(s1), len(s2)
        min_len = float('inf')
        min_start = -1
        i = 0
        while i < n:
            if s1[i] == s2[0]:
                start = i
                j = 1
                while i < n and j < m:
                    i += 1
                    if i < n and s1[i] == s2[j]:
                        j += 1
                if j == m:
                    end = i + 1
                    j -= 1
                    while j >= 0:
                        if s1[i] == s2[j]:
                            j -= 1
                        i -= 1
                    i += 1  
                    if end - i < min_len:
                        min_len = end - i
                        min_start = i
                else:
                    break
            i += 1
        return "" if min_start == -1 else s1[min_start:min_start + min_len]
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("abcdebdde", "bde", "bcde"),
        ("jmeqksfrsdcmsiwvaovztaqenprpvnbstl", "u", ""),
        ("abc", "abc", "abc"),
        ("abc", "acb", ""),
        ("aaaaaaaaaaaaaaaaaaaabbbbbbbbbbbb", "aaaaaaaaaaaaaaabbb", "aaaaaaaaaaaaaaabbb"),
    ]
    for idx, (s1, s2, expected) in enumerate(test_cases, 1):
        result = solution.minWindow(s1, s2)
        status = "PASS" if result == expected else "FAIL"
        print("Test %d: [%s]" % (idx, status))
        print("  Input:    s1 = \"%s\", s2 = \"%s\"" % (s1, s2))
        print("  Output:   \"%s\"" % result)
        print("  Expected: \"%s\"" % expected)
        print("")
print(__name__)