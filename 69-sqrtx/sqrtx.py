class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        left, right = 1, x // 2
        result = 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                result = mid      
                left = mid + 1
            else:
                right = mid - 1
        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(4))   
    print(sol.mySqrt(8))  
    print(sol.mySqrt(0))  
    print(sol.mySqrt(1))  
    print(sol.mySqrt(2147483647)) 
print(__name__)