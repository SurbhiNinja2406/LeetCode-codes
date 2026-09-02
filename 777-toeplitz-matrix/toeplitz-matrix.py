class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True
if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    print("Input: matrix = {}".format(matrix))
    print("Output: {}".format(sol.isToeplitzMatrix(matrix)))
    print("Expected: True\n")
    matrix = [[1, 2], [2, 2]]
    print("Input: matrix = {}".format(matrix))
    print("Output: {}".format(sol.isToeplitzMatrix(matrix)))
    print("Expected: False\n")
print(__name__)