class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def backtrack(current, open_count, close_count):
            if len(current) == 2 * n:
                result.append(''.join(current))
                return
            if open_count < n:
                current.append('(')
                backtrack(current, open_count + 1, close_count)
                current.pop()  
            if close_count < open_count:
                current.append(')')
                backtrack(current, open_count, close_count + 1)
                current.pop() 
        backtrack([], 0, 0)
        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(3))
    print(sol.generateParenthesis(1))
    print(sol.generateParenthesis(2))
    print(sol.generateParenthesis(4))
    print(sol.generateParenthesis(8))
print(__name__)