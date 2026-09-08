import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """        
        def hours_needed(speed):
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / float(speed))
            return total_hours
        low = 1
        high = max(piles)
        while low < high:
            mid = (low + high) // 2
            if hours_needed(mid) <= h:
                high = mid
            else:
                low = mid + 1        
        return low
if __name__ == "__main__":
    sol = Solution()
    piles1, h1 = [3, 6, 7, 11], 8
    result1 = sol.minEatingSpeed(piles1, h1)
    print("Example 1:")
    print("Input: piles = {}, h = {}".format(piles1, h1))
    print("Output:", result1)
    print("Expected: 4")
    print()
    piles2, h2 = [30, 11, 23, 4, 20], 5
    result2 = sol.minEatingSpeed(piles2, h2)
    print("Example 2:")
    print("Input: piles = {}, h = {}".format(piles2, h2))
    print("Output:", result2)
    print("Expected: 30")
    print()
    piles3, h3 = [30, 11, 23, 4, 20], 6
    result3 = sol.minEatingSpeed(piles3, h3)
    print("Example 3:")
    print("Input: piles = {}, h = {}".format(piles3, h3))
    print("Output:", result3)
    print("Expected: 23")
    print()
    piles4, h4 = [1000000000], 2
    result4 = sol.minEatingSpeed(piles4, h4)
    print("Additional test (single large pile):")
    print("Input: piles = {}, h = {}".format(piles4, h4))
    print("Output:", result4)
    print("Expected: 500000000")
print(__name__)