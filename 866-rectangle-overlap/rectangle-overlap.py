class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        x_overlap = x1 < x4 and x3 < x2
        y_overlap = y1 < y4 and y3 < y2        
        return x_overlap and y_overlap
if __name__ == "__main__":
    sol = Solution()
    print(sol.isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3])) 
    print(sol.isRectangleOverlap([0, 0, 1, 1], [1, 0, 2, 1]))  
    print(sol.isRectangleOverlap([0, 0, 1, 1], [2, 2, 3, 3]))  
print(__name__)