class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0] 
        for char in s:
            if char == '(':
                stack.append(0)
            else: 
                inner_score = stack.pop()
                if inner_score == 0:
                    completed_score = 1
                else:
                    completed_score = 2 * inner_score
                stack[-1] += completed_score
        return stack[0]
if __name__ == "__main__":
    solution = Solution()
    s1 = "()"
    print(solution.scoreOfParentheses(s1)) 
    s2 = "(())"
    print(solution.scoreOfParentheses(s2))  
    s3 = "()()"
    print(solution.scoreOfParentheses(s3))  
    s4 = "(()(()))"
    print(solution.scoreOfParentheses(s4)) 
    s5 = "((()))"
    print(solution.scoreOfParentheses(s5))  
    s6 = "()(())"
    print(solution.scoreOfParentheses(s6)) 