class Solution(object):
    def pourWater(self, heights, volume, k):
        """
        :type heights: List[int]
        :type volume: int
        :type k: int
        :rtype: List[int]
        """
        n = len(heights)
        for _ in range(volume):
            best = k  
            i = k
            while i - 1 >= 0 and heights[i - 1] <= heights[i]:
                if heights[i - 1] < heights[i]:
                    best = i - 1
                i -= 1
            if best != k:
                heights[best] += 1
                continue
            i = k
            while i + 1 < n and heights[i + 1] <= heights[i]:
                if heights[i + 1] < heights[i]:
                    best = i + 1
                i += 1
            heights[best] += 1
        return heights
if __name__ == "__main__":
    sol = Solution()
    print(sol.pourWater([2, 1, 1, 2, 1, 2, 2], 4, 3))
    print(sol.pourWater([1, 2, 3, 4], 2, 2))
    print(sol.pourWater([3, 1, 3], 5, 1))
print(__name__)