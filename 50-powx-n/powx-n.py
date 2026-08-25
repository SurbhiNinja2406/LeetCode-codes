class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n        
        return self._fastPow(x, n)    
    def _fastPow(self, x, n):
        if n == 0:
            return 1.0        
        half = self._fastPow(x, n // 2)        
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
if __name__ == "__main__":
    solution = Solution()
    x1, n1 = 2.00000, 10
    print(solution.myPow(x1, n1))  
    x2, n2 = 2.10000, 3
    print(solution.myPow(x2, n2))  
    x3, n3 = 2.00000, -2
    print(solution.myPow(x3, n3)) 