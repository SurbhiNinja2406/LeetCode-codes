class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([1, 2, 3]))   
    print(sol.plusOne([4, 3, 2, 1])) 
    print(sol.plusOne([9]))          
    print(sol.plusOne([9, 9, 9]))  
print(__name__)