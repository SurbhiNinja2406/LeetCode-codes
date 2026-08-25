class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1] * (rowIndex + 1)
        for i in range(1, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j - 1]
        return row
if __name__ == "__main__":
    sol = Solution()
    print("Test 1: {}".format(sol.getRow(3))) 
    print("Test 2: {}".format(sol.getRow(0))) 
    print("Test 3: {}".format(sol.getRow(1)))  
print(__name__)