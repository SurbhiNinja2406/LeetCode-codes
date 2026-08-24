class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            result = result * 10 + digit
            i += 1
        result *= sign
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.myAtoi("42"))  
    print(sol.myAtoi("   -042")) 
    print(sol.myAtoi("1337c0d3"))  
    print(sol.myAtoi("0-1")) 
    print(sol.myAtoi("words and 987"))  
    print(sol.myAtoi(""))  
    print(sol.myAtoi("   "))  
    print(sol.myAtoi("+"))  
    print(sol.myAtoi("91283472332")) 
    print(sol.myAtoi("-91283472332")) 
    print(sol.myAtoi("00000-42a1234")) 
    print(sol.myAtoi("+1")) 
    print(sol.myAtoi("   +0 123"))  