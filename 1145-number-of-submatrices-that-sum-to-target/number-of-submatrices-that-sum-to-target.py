from collections import defaultdict

class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        count = 0
        for top in range(m):
            col_sums = [0] * n  
            for bottom in range(top, m):
                for c in range(n):
                    col_sums[c] += matrix[bottom][c]
                seen = defaultdict(int)
                seen[0] = 1 
                prefix = 0
                for v in col_sums:
                    prefix += v
                    count += seen.get(prefix - target, 0)
                    seen[prefix] += 1
        return count
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0),
        ([[1, -1], [-1, 1]], 0),           
        ([[904]], 0),                        
    ]
    for mat, t in tests:
        print("matrix = {}, target = {} -> {}".format(mat, t, sol.numSubmatrixSumTarget(mat, t)))
print(__name__)