class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math        
        numbers = [str(i) for i in range(1, n + 1)]
        result = []
        k -= 1
        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            index = k // fact            
            result.append(numbers[index])
            numbers.pop(index)
            k %= fact        
        return "".join(result)
if __name__ == "__main__":
    solution = Solution()
    n1, k1 = 3, 3
    print(solution.getPermutation(n1, k1)) 
    n2, k2 = 4, 9
    print(solution.getPermutation(n2, k2))  
    n3, k3 = 3, 1
    print(solution.getPermutation(n3, k3)) 
print(__name__)