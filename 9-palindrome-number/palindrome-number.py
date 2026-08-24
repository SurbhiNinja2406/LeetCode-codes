class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x != 0 and x % 10 == 0:
            return False
        original = x
        reversed_num = 0
        while x != 0:
            digit = x % 10
            x //= 10
            reversed_num = reversed_num * 10 + digit
        return original == reversed_num
if __name__ == "__main__":
    sol = Solution()
    x1 = 121
    expected1 = True
    result1 = sol.isPalindrome(x1)
    print("Example 1")
    print("  input:   ", x1)
    print("  output:  ", result1)
    print("  expected:", expected1)
    print("  PASS" if result1 == expected1 else "  FAIL")
    print()
    x2 = -121
    expected2 = False
    result2 = sol.isPalindrome(x2)
    print("Example 2")
    print("  input:   ", x2)
    print("  output:  ", result2)
    print("  expected:", expected2)
    print("  PASS" if result2 == expected2 else "  FAIL")
    print()
    x3 = 10
    expected3 = False
    result3 = sol.isPalindrome(x3)
    print("Example 3")
    print("  input:   ", x3)
    print("  output:  ", result3)
    print("  expected:", expected3)
    print("  PASS" if result3 == expected3 else "  FAIL")
    print()
    print("x=7       ->", sol.isPalindrome(7), "(expect True, single digit)")
    print("x=0       ->", sol.isPalindrome(0), "(expect True)")
    print("x=1221    ->", sol.isPalindrome(1221), "(expect True)")
    print("x=1234321 ->", sol.isPalindrome(1234321), "(expect True)")
    print("x=123456  ->", sol.isPalindrome(123456), "(expect False)")