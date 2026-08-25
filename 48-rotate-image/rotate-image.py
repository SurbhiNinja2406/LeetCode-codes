class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
def print_matrix(matrix):
    for row in matrix:
        print(row)
if __name__ == "__main__":
    solution = Solution()
    matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
    solution.rotate(matrix1)
    print_matrix(matrix1)    
    print()
    matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    solution.rotate(matrix2)
    print_matrix(matrix2)
print(__name__)