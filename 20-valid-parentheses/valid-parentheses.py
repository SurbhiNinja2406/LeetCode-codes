class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for char in s:
            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0
if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()")) 
    print(sol.isValid("()[]{}"))
    print(sol.isValid("(]")) 
    print(sol.isValid("([])")) 
    print(sol.isValid("([)]"))  
    print(sol.isValid("("))  
    print(sol.isValid(")")) 
    print(sol.isValid("((({{{[[[]]]}}})))")) 
    print(sol.isValid("]")) 
    print(sol.isValid("{[}")) 