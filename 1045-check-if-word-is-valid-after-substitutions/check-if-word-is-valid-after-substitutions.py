class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            stack.append(char)
            if len(stack) >= 3 and stack[-3] == 'a' and stack[-2] == 'b' and stack[-1] == 'c':
                stack.pop()
                stack.pop()
                stack.pop()
        return len(stack) == 0
if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("aabcbc"))  
    print(sol.isValid("abcabcababcc")) 
    print(sol.isValid("aabcbc"))         
    print(sol.isValid("abcabcababcc"))   
    print(sol.isValid("abccba"))        
print(__name__)