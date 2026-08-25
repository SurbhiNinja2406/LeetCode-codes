class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for row_num in range(numRows):
            row = [1] * (row_num + 1)
            for j in range(1, row_num):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
            triangle.append(row)
        return triangle
if __name__ == "__main__":
    sol = Solution()
    print("Test 1: {}".format(sol.generate(5)))
    print("Test 2: {}".format(sol.generate(1))) 
print(__name__)