class Solution(object):
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        xs = sorted(set(x for rect in rectangles for x in (rect[0], rect[2])))
        ys = sorted(set(y for rect in rectangles for y in (rect[1], rect[3])))
        x_index = {x: i for i, x in enumerate(xs)}
        y_index = {y: i for i, y in enumerate(ys)}
        cols = len(xs) - 1
        rows = len(ys) - 1
        if cols <= 0 or rows <= 0:
            return 0
        covered = [[False] * rows for _ in range(cols)]
        for x1, y1, x2, y2 in rectangles:
            i1, i2 = x_index[x1], x_index[x2]
            j1, j2 = y_index[y1], y_index[y2]
            for i in range(i1, i2):
                for j in range(j1, j2):
                    covered[i][j] = True
        total_area = 0
        for i in range(cols):
            width = xs[i + 1] - xs[i]
            for j in range(rows):
                if covered[i][j]:
                    height = ys[j + 1] - ys[j]
                    total_area = (total_area + width * height) % MOD
        return total_area % MOD
if __name__ == "__main__":
    solution = Solution()
    rectangles1 = [[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]
    print(solution.rectangleArea(rectangles1))  
    rectangles2 = [[0, 0, 1000000000, 1000000000]]
    print(solution.rectangleArea(rectangles2))  
    rectangles3 = [[0, 0, 1, 1], [2, 2, 3, 3]]
    print(solution.rectangleArea(rectangles3))  
    rectangles4 = [[0, 0, 5, 5], [0, 0, 5, 5]]
    print(solution.rectangleArea(rectangles4)) 
    rectangles5 = [[0, 0, 3, 4]]
    print(solution.rectangleArea(rectangles5)) 
    rectangles6 = [[0, 0, 2, 2], [2, 0, 4, 2]]
    print(solution.rectangleArea(rectangles6)) 
print(__name__)