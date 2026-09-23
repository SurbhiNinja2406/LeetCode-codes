class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Base cases
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        t0, t1, t2 = 0, 1, 1        
        for _ in range(3, n + 1):
            t0, t1, t2 = t1, t2, t0 + t1 + t2        
        return t2
if __name__ == "__main__":
    sol = Solution()
    print(sol.tribonacci(4))  
    print(sol.tribonacci(25))  
print(__name__)