class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        point_set = set()
        for x, y in points:
            point_set.add((x, y))
        min_area = float('inf')
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                if x1 == x2 or y1 == y2:
                    continue
                if (x1, y2) in point_set and (x2, y1) in point_set:
                    area = abs(x2 - x1) * abs(y2 - y1)
                    min_area = min(min_area, area)
        return min_area if min_area != float('inf') else 0
if __name__ == "__main__":
    sol = Solution()
    points1 = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
    print(sol.minAreaRect(points1)) 
    points2 = [[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]
    print(sol.minAreaRect(points2)) 
    points3 = [[1, 1], [2, 2], [3, 3]]
    print(sol.minAreaRect(points3)) 
print(__name__)