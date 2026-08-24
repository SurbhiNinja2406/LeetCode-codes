class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        negative = (dividend < 0) != (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple
        if negative:
            quotient = -quotient
        if quotient < INT_MIN:
            return INT_MIN
        if quotient > INT_MAX:
            return INT_MAX
        return quotient
if __name__ == "__main__":
    sol = Solution()
    print(sol.divide(10, 3)) 
    print(sol.divide(7, -3))  
    print(sol.divide(-2147483648, -1))  
    print(sol.divide(10, 2))  
    print(sol.divide(3, 10)) 
    print(sol.divide(-10, -3)) 
    print(sol.divide(15, 1))  
    print(sol.divide(15, -1)) 
    print(sol.divide(0, 5))  
    print(sol.divide(1000000000, 1)) 