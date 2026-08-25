class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in range(n)]        
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1        
        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = num
                    num += 1
                bottom -= 1
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = num
                    num += 1
                left += 1        
        return matrix
if __name__ == "__main__":
    solution = Solution()
    n1 = 3
    print(solution.generateMatrix(n1))  
    n2 = 1
    print(solution.generateMatrix(n2))  
print(__name__)