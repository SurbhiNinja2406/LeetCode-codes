class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        min_repeats = -(-len(b) // len(a))  
        candidate = a * min_repeats
        if b in candidate:
            return min_repeats
        candidate += a
        if b in candidate:
            return min_repeats + 1
        return -1
if __name__ == "__main__":
    solution = Solution()
    result1 = solution.repeatedStringMatch("abcd", "cdabcdab")
    print("Example 1:")
    print('Input:  a = "abcd", b = "cdabcdab"')
    print("Output:", result1)
    print("Expected: 3")
    print()
    result2 = solution.repeatedStringMatch("a", "aa")
    print("Example 2:")
    print('Input:  a = "a", b = "aa"')
    print("Output:", result2)
    print("Expected: 2")
    print()
    result3 = solution.repeatedStringMatch("abcd", "bc")
    print("Example 3 (extra):")
    print('Input:  a = "abcd", b = "bc"')
    print("Output:", result3)
    print("Expected: 1")
    print()
    result4 = solution.repeatedStringMatch("abc", "wxyz")
    print("Example 4 (extra):")
    print('Input:  a = "abc", b = "wxyz"')
    print("Output:", result4)
    print("Expected: -1")
    print()
    result5 = solution.repeatedStringMatch("ab", "ababab")
    print("Example 5 (extra):")
    print('Input:  a = "ab", b = "ababab"')
    print("Output:", result5)
    print("Expected: 3")
    print()
    result6 = solution.repeatedStringMatch("abc", "cabcabca")
    print("Example 6 (extra):")
    print('Input:  a = "abc", b = "cabcabca"')
    print("Output:", result6)
print(__name__)