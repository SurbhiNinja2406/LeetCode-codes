import math
from collections import defaultdict
class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        pts = [tuple(p) for p in points]
        n = len(pts)        
        if n < 4:
            return 0.0
        groups = defaultdict(list)        
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = pts[i]
                x2, y2 = pts[j]
                center = (x1 + x2, y1 + y2)
                dist_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2
                key = (center[0], center[1], dist_sq)
                groups[key].append((pts[i], pts[j]))
        def distance(p, q):
            return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)        
        min_area = float('inf')        
        for key, pairs in groups.items():
            if len(pairs) < 2:
                continue
            for a in range(len(pairs)):
                for b in range(a + 1, len(pairs)):
                    p1, p2 = pairs[a]
                    p3, p4 = pairs[b]
                    side1 = distance(p1, p3)
                    side2 = distance(p1, p4)
                    area = side1 * side2
                    min_area = min(min_area, area)        
        return min_area if min_area != float('inf') else 0.0
if __name__ == "__main__":
    sol = Solution()
    points1 = [[1, 2], [2, 1], [1, 0], [0, 1]]
    result1 = sol.minAreaFreeRect(points1)
    print("Input: {}".format(points1))
    print("Output: {:.5f}".format(result1))
    print("Expected: 2.00000")
    print("Pass: {}\n".format(abs(result1 - 2.0) < 1e-5))
    points2 = [[0, 1], [2, 1], [1, 1], [1, 0], [2, 0]]
    result2 = sol.minAreaFreeRect(points2)
    print("Input: {}".format(points2))
    print("Output: {:.5f}".format(result2))
    print("Expected: 1.00000")
    print("Pass: {}\n".format(abs(result2 - 1.0) < 1e-5))
    points3 = [[0, 3], [1, 2], [3, 1], [1, 3], [2, 1]]
    result3 = sol.minAreaFreeRect(points3)
    print("Input: {}".format(points3))
    print("Output: {:.5f}".format(result3))
    print("Expected: 0.00000")
    print("Pass: {}\n".format(abs(result3 - 0.0) < 1e-5))
    points4 = [[0, 0], [1, 1], [2, 2]]
    result4 = sol.minAreaFreeRect(points4)
    print("Input: {}".format(points4))
    print("Output: {:.5f}".format(result4))
    print("Expected: 0.00000")
    print("Pass: {}\n".format(abs(result4 - 0.0) < 1e-5))
    points5 = [[0, 0], [0, 2], [2, 0], [2, 2]]
    result5 = sol.minAreaFreeRect(points5)
    print("Input: {}".format(points5))
    print("Output: {:.5f}".format(result5))
    print("Expected: 4.00000")
    print("Pass: {}\n".format(abs(result5 - 4.0) < 1e-5))
    points6 = [[0, 0], [1, 1], [2, 2], [3, 3]]
    result6 = sol.minAreaFreeRect(points6)
    print("Input: {}".format(points6))
    print("Output: {:.5f}".format(result6))
    print("Expected: 0.00000")
    print("Pass: {}\n".format(abs(result6 - 0.0) < 1e-5))
print(__name__)