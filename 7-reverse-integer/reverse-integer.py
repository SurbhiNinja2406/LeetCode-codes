class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        sign = -1 if x < 0 else 1
        x = abs(x)
        result = 0
        while x != 0:
            digit = x % 10
            x //= 10
            result = result * 10 + digit
        result *= sign
        if result < INT_MIN or result > INT_MAX:
            return 0
        return result
if __name__ == "__main__":
    sol = Solution()
    x = 123
    print(sol.reverse(x))  
    x = -123
    print(sol.reverse(x))
    x = 120
    print(sol.reverse(x)) 
    x = 0
    print(sol.reverse(x))  
    x = 1534236469
    print(sol.reverse(x))  
    x = 1463847412
    print(sol.reverse(x))  
    x = -1563847412
    print(sol.reverse(x))