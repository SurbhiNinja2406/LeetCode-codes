class Solution(object):
    def clumsy(self, n):
        """
        :type n: int
        :rtype: int
        """
        stack = [n]
        num = n - 1
        op_index = 0
        while num >= 1:
            op = op_index % 4
            if op == 0:  
                stack.append(stack.pop() * num)
            elif op == 1: 
                stack.append(int(stack.pop() * 1.0 / num))
            elif op == 2:  
                stack.append(num)
            else:  
                stack.append(-num)
            op_index += 1
            num -= 1
        return sum(stack)
if __name__ == "__main__":
    sol = Solution()
    print(sol.clumsy(4))  
    print(sol.clumsy(10)) 
print(__name__)