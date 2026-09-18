class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        stack = []
        for ch in expression:
            if ch == ',':
                continue  
            if ch != ')':
                stack.append(ch)
            else:
                operands = []
                while stack[-1] != '(':
                    operands.append(stack.pop())
                stack.pop()  
                operator = stack.pop()  
                if operator == '!':
                    result = (operands[0] == 'f')
                elif operator == '&':
                    result = all(op == 't' for op in operands)
                elif operator == '|':
                    result = any(op == 't' for op in operands)
                stack.append('t' if result else 'f')
        return stack[-1] == 't'
if __name__ == "__main__":
    sol = Solution()
    print(sol.parseBoolExpr("&(|(f))"))   
    print(sol.parseBoolExpr("|(f,f,f,t)"))  
    print(sol.parseBoolExpr("!(&(f,t))"))    
print(__name__)