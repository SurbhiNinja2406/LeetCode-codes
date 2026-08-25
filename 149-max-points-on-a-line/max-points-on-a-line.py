from collections import defaultdict


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a        
        n = len(points)        
        if n <= 2:
            return n
        max_count = 1        
        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]            
            for j in range(n):
                if i == j:
                    continue                
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1                
                if dx == 0:
                    key = ('inf', 0)
                else:
                    g = gcd(abs(dx), abs(dy))
                    if g != 0:
                        dx //= g
                        dy //= g
                    if dx < 0:
                        dx, dy = -dx, -dy
                    key = (dx, dy)                
                slopes[key] += 1            
            if slopes:
                local_max = max(slopes.values()) + 1
                max_count = max(max_count, local_max)        
        return max_count
if __name__ == "__main__":
    sol = Solution()    
    points1 = [[1, 1], [2, 2], [3, 3]]
    print(sol.maxPoints(points1)) 
    points2 = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    print(sol.maxPoints(points2))  
print(__name__)