class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = n ^ (n >> 1)
        return (x & (x + 1)) == 0
if __name__ == "__main__":
    sol = Solution()
    print(sol.hasAlternatingBits(5))  
    print(sol.hasAlternatingBits(7))  
    print(sol.hasAlternatingBits(11))  
    print(sol.hasAlternatingBits(10)) 
    print(sol.hasAlternatingBits(1))   
print(__name__)