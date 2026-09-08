class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)    
        n = len(matrix[0])  
        result = [[0] * m for _ in range(n)]        
        for i in range(m):
            for j in range(n):
                result[j][i] = matrix[i][j]        
        return result
if __name__ == "__main__":
    sol = Solution()
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result1 = sol.transpose(matrix1)
    print("Example 1:")
    print("Input: matrix = {}".format(matrix1))
    print("Output:", result1)
    print("Expected: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]")
    print()
    matrix2 = [[1, 2, 3], [4, 5, 6]]
    result2 = sol.transpose(matrix2)
    print("Example 2:")
    print("Input: matrix = {}".format(matrix2))
    print("Output:", result2)
    print("Expected: [[1, 4], [2, 5], [3, 6]]")
    print()
    matrix3 = [[1, 2, 3, 4]]
    result3 = sol.transpose(matrix3)
    print("Additional test (single row):")
    print("Input: matrix = {}".format(matrix3))
    print("Output:", result3)
    print("Expected: [[1], [2], [3], [4]]")
    print()
    matrix4 = [[1], [2], [3]]
    result4 = sol.transpose(matrix4)
    print("Additional test (single column):")
    print("Input: matrix = {}".format(matrix4))
    print("Output:", result4)
    print("Expected: [[1, 2, 3]]")