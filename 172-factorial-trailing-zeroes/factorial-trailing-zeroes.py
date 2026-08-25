class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        power_of_5 = 5
        while power_of_5 <= n:
            count += n // power_of_5
            power_of_5 *= 5
        return count
if __name__ == "__main__":
    sol = Solution()
    print(sol.trailingZeroes(3))   
    print(sol.trailingZeroes(5))  
    print(sol.trailingZeroes(0)) 
    print(sol.trailingZeroes(25))  
print(__name__)