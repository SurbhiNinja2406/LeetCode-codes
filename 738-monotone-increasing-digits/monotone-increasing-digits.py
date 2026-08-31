class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = list(str(n))
        marker = len(digits)  
        for i in range(len(digits) - 1, 0, -1):
            if digits[i - 1] > digits[i]:
                digits[i - 1] = str(int(digits[i - 1]) - 1)
                marker = i
        for i in range(marker, len(digits)):
            digits[i] = '9'
        return int(''.join(digits))
if __name__ == "__main__":
    sol = Solution()
    print(sol.monotoneIncreasingDigits(10))
    print(sol.monotoneIncreasingDigits(1234))
    print(sol.monotoneIncreasingDigits(332))
print(__name__)