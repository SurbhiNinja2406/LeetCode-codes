class Solution(object):
    def confusingNumber(self, n):
        """
        :type n: int
        :rtype: bool
        """
        rotate = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        original = n
        rotated = 0
        while n > 0:
            digit = n % 10
            if digit not in rotate:
                return False
            rotated = rotated * 10 + rotate[digit]
            n //= 10
        return rotated != original
if __name__ == "__main__":
    sol = Solution()
    print(sol.confusingNumber(6))  
    print(sol.confusingNumber(89))   
    print(sol.confusingNumber(11))  
    print(sol.confusingNumber(25))  
    print(sol.confusingNumber(8000))  
    print(sol.confusingNumber(0))   
print(__name__)