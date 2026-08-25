class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1        
        while left <= right:
            mid = (left + right) // 2
            row, col = divmod(mid, n)
            mid_val = matrix[row][col]            
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
if __name__ == "__main__":
    sol = Solution()
    matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(sol.searchMatrix(matrix1, 3))  
    matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(sol.searchMatrix(matrix2, 13)) 
print(__name__)