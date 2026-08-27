class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        low = 0
        high = 0
        for ch in s:
            if ch == '(':
                low += 1
                high += 1
            elif ch == ')':
                low -= 1
                high -= 1
            else: 
                low -= 1  
                high += 1  
            if high < 0:
                return False
            low = max(low, 0)
        return low == 0
if __name__ == "__main__":
    solution = Solution()
    result1 = solution.checkValidString("()")
    print("Example 1:")
    print('Input:  s = "()"')
    print("Output:", result1)
    print("Expected: True")
    print()
    result2 = solution.checkValidString("(*)")
    print("Example 2:")
    print('Input:  s = "(*)"')
    print("Output:", result2)
    print("Expected: True")
    print()
    result3 = solution.checkValidString("(*))")
    print("Example 3:")
    print('Input:  s = "(*))"')
    print("Output:", result3)
    print("Expected: True")
    print()
    result4 = solution.checkValidString("(()")
    print("Example 4 (extra):")
    print('Input:  s = "(()"')
    print("Output:", result4)
    print("Expected: False")
    print()

    # All stars -- can always be empty
    result5 = solution.checkValidString("***")
    print("Example 5 (extra):")
    print('Input:  s = "***"')
    print("Output:", result5)
    print("Expected: True")
    print()

    # Star before too many closing parens
    result6 = solution.checkValidString("*)))")
    print("Example 6 (extra):")
    print('Input:  s = "*)))"')
    print("Output:", result6)
    print("Expected: False")
    print()

    # Single star
    result7 = solution.checkValidString("*")
    print("Example 7 (extra):")
    print('Input:  s = "*"')
    print("Output:", result7)
    print("Expected: True")
print(__name__)