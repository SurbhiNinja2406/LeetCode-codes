class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = {'+', '-', '*', '/'}        
        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                else:  
                    result = int(a / b) if (a * b) >= 0 else -(-a // b) if a < 0 else -(a // -b)                
                stack.append(result)
            else:
                stack.append(int(token))        
        return stack[0]
if __name__ == "__main__":
    sol = Solution()
    tokens1 = ["2", "1", "+", "3", "*"]
    print(sol.evalRPN(tokens1)) 
    tokens2 = ["4", "13", "5", "/", "+"]
    print(sol.evalRPN(tokens2)) 
    tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(sol.evalRPN(tokens3)) 
print(__name__)