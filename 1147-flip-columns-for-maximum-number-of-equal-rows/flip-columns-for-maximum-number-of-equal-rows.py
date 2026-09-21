from collections import Counter

class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        counts = Counter()
        for row in matrix:
            first = row[0]
            pattern = tuple(cell ^ first for cell in row)
            counts[pattern] += 1
        return max(counts.values())
if __name__ == "__main__":
    sol = Solution()
    tests = [
        [[0, 1], [1, 1]],    
        [[0, 1], [1, 0]],              
        [[0, 0, 0], [0, 0, 1], [1, 1, 0]],  
    ]
    for m in tests:
        print("matrix = {} -> {}".format(m, sol.maxEqualRowsAfterFlips(m)))
print(__name__)