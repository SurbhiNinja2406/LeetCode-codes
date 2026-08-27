class Solution(object):
    def kEmptySlots(self, bulbs, k):
        """
        :type bulbs: List[int]
        :type k: int
        :rtype: int
        """
        n = len(bulbs)
        if k >= n:
            return -1
        days = [0] * n
        for day, pos in enumerate(bulbs, 1):
            days[pos - 1] = day
        left, right = 0, k + 1
        ans = float('inf')
        while right < n:
            found_smaller_in_between = False
            for j in range(left + 1, right):
                if days[j] < days[left] or days[j] < days[right]:
                    left = j
                    right = j + k + 1
                    found_smaller_in_between = True
                    break
            if not found_smaller_in_between:
                ans = min(ans, max(days[left], days[right]))
                left = right
                right = left + k + 1
        return ans if ans != float('inf') else -1
if __name__ == "__main__":
    solution = Solution()
    result1 = solution.kEmptySlots([1, 3, 2], 1)
    print("Example 1:")
    print("Input:  bulbs = [1,3,2], k = 1")
    print("Output:", result1)
    print("Expected: 2")
    print()
    result2 = solution.kEmptySlots([1, 2, 3], 1)
    print("Example 2:")
    print("Input:  bulbs = [1,2,3], k = 1")
    print("Output:", result2)
    print("Expected: -1")
    print()
    result3 = solution.kEmptySlots([1, 2], 0)
    print("Example 3 (extra):")
    print("Input:  bulbs = [1,2], k = 0")
    print("Output:", result3)
    print("Expected: 2")
    print()
    result4 = solution.kEmptySlots([1, 2, 3], 5)
    print("Example 4 (extra):")
    print("Input:  bulbs = [1,2,3], k = 5")
    print("Output:", result4)
    print("Expected: -1")
    print()
    result5 = solution.kEmptySlots([1, 3, 5, 4, 2], 1)
    print("Example 5 (extra):")
    print("Input:  bulbs = [1,3,5,4,2], k = 1")
    print("Output:", result5)
print(__name__)