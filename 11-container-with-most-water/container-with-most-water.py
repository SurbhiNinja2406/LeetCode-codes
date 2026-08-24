class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_water = 0
        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            max_water = max(max_water, width * current_height)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])) 
    print(sol.maxArea([1, 1])) 
    print(sol.maxArea([1, 2, 3, 4, 5])) 
    print(sol.maxArea([5, 5, 5, 5, 5]))  
    print(sol.maxArea([6, 1, 2, 3, 4, 5, 6]))  
    print(sol.maxArea([4, 3]))  