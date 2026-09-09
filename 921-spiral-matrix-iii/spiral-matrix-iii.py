class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        total = rows * cols
        result = [[rStart, cStart]]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r, c = rStart, cStart
        dir_index = 0
        step_size = 1
        while len(result) < total:
            for _ in range(2):
                dr, dc = directions[dir_index]
                for _ in range(step_size):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                        if len(result) == total:
                            return result
                dir_index = (dir_index + 1) % 4
            step_size += 1
        return result
if __name__ == "__main__":
    sol = Solution()
    rows1, cols1, rStart1, cStart1 = 1, 4, 0, 0
    result1 = sol.spiralMatrixIII(rows1, cols1, rStart1, cStart1)
    print("Example 1: {}".format(result1))
    print("Expected 1: [[0,0],[0,1],[0,2],[0,3]]")
    print()
    rows2, cols2, rStart2, cStart2 = 5, 6, 1, 4
    result2 = sol.spiralMatrixIII(rows2, cols2, rStart2, cStart2)
    print("Example 2: {}".format(result2))
    print("Expected 2: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],"
          "[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],"
          "[3,0],[2,0],[1,0],[0,0]]")