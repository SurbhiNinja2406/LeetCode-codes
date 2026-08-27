class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_palindrome_range(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return (is_palindrome_range(left + 1, right) or
                        is_palindrome_range(left, right - 1))
            left += 1
            right -= 1
        return True
if __name__ == "__main__":
    solution = Solution()
    result1 = solution.validPalindrome("aba")
    print("Example 1:")
    print('Input:  s = "aba"')
    print("Output:", result1)
    print("Expected: True")
    print()
    result2 = solution.validPalindrome("abca")
    print("Example 2:")
    print('Input:  s = "abca"')
    print("Output:", result2)
    print("Expected: True")
    print()
    result3 = solution.validPalindrome("abc")
    print("Example 3:")
    print('Input:  s = "abc"')
    print("Output:", result3)
    print("Expected: False")
    print()
    result4 = solution.validPalindrome("a")
    print("Example 4 (extra):")
    print('Input:  s = "a"')
    print("Output:", result4)
    print("Expected: True")
    print()
    result5 = solution.validPalindrome("racecar")
    print("Example 5 (extra):")
    print('Input:  s = "racecar"')
    print("Output:", result5)
    print("Expected: True")
    print()
    result6 = solution.validPalindrome("eeccccbebaeeabebccceea")
    print("Example 6 (extra):")
    print('Input:  s = "eeccccbebaeeabebccceea"')
    print("Output:", result6)
    print("Expected: True")
    print()
    result7 = solution.validPalindrome("abcdba")
    print("Example 7 (extra):")
    print('Input:  s = "abcdba"')
    print("Output:", result7)
    print("Expected: False")
print(__name__)