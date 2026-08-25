class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [] 
        max_area = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))
        for index, height in stack:
            max_area = max(max_area, height * (len(heights) - index))
        return max_area
if __name__ == "__main__":
    sol = Solution()
    print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3])) 
    print(sol.largestRectangleArea([2, 4]))  
print(__name__)    