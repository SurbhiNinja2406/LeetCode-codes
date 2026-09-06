class Solution(object):
    def consecutiveNumbersSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        k = 1
        while k * (k - 1) // 2 < n:
            remainder = n - k * (k - 1) // 2
            if remainder % k == 0:
                count += 1
            k += 1
        return count
if __name__ == "__main__":
    sol = Solution()
    print(sol.consecutiveNumbersSum(5)) 
    print(sol.consecutiveNumbersSum(9))  
    print(sol.consecutiveNumbersSum(15))  
print(__name__)