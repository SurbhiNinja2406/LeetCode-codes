class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]
        for i in range(n):
            result += [x + (1 << i) for x in reversed(result)]
        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.grayCode(2))  
    print(sol.grayCode(1)) 
    print(sol.grayCode(3)) 
print(__name__)