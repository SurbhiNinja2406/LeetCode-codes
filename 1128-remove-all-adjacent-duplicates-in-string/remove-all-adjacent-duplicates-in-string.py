class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()       
            else:
                stack.append(ch)
        return "".join(stack)
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("abbaca", "ca"),
        ("azxxzy", "ay"),
        ("aa", ""),         
        ("abcd", "abcd"),    
    ]
    for s, expected in tests:
        result = sol.removeDuplicates(s)
        status = "PASS" if result == expected else "FAIL"
        print("{}: got '{}', expected '{}'".format(status, result, expected))
print(__name__)