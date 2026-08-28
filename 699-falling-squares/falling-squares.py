class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        placed = []
        result = []
        max_height_so_far = 0
        for left, side_length in positions:
            right = left + side_length
            base = 0
            for p_left, p_right, p_top in placed:
                if left < p_right and p_left < right:
                    base = max(base, p_top)
            top = base + side_length
            placed.append((left, right, top))
            max_height_so_far = max(max_height_so_far, top)
            result.append(max_height_so_far)
        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.fallingSquares([[1,2],[2,3],[6,1]]))    
    print(sol.fallingSquares([[100,100],[200,100]])) 
print(__name__)