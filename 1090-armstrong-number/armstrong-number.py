class Solution(object):
    def isArmstrong(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digits = str(n)
        k = len(digits)
        total = sum(int(d) ** k for d in digits)        
        return total == n
if __name__ == "__main__":
    sol = Solution()
    print(sol.isArmstrong(153))  
    print(sol.isArmstrong(123))  
print(__name__)