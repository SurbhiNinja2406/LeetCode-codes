class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        pop_index = 0
        for num in pushed:
            stack.append(num)
            while stack and pop_index < len(popped) and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1
        return pop_index == len(popped)
if __name__ == "__main__":
    sol = Solution()
    print(sol.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))  
    print(sol.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2])) 
print(__name__)