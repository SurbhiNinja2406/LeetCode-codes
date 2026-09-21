class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""
        a, b = len(str1), len(str2)
        while b:
            a, b = b, a % b
        return str1[:a]
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("ABCABC", "ABC"),
        ("ABABAB", "ABAB"),
        ("LEET", "CODE"),
        ("AAAAAB", "AAA"),
    ]
    for s1, s2 in tests:
        print('str1 = "{}", str2 = "{}" -> "{}"'.format(s1, s2, sol.gcdOfStrings(s1, s2)))
print(__name__)