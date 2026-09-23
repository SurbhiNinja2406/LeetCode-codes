class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = [float('inf')]
        res = 0
        for a in arr:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res
if __name__ == "__main__":
    sol = Solution()
    arr1 = [6, 2, 4]
    print(sol.mctFromLeafValues(arr1))  
    arr2 = [4, 11]
    print(sol.mctFromLeafValues(arr2))  
print(__name__)