class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        first, second = 1, 2  
        for i in range(3, n + 1):
            first, second = second, first + second
        return second
if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(2))   
    print(sol.climbStairs(3))  
    print(sol.climbStairs(4))  
    print(sol.climbStairs(45))  
print(__name__)