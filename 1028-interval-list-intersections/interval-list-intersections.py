class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]
            lo = max(a_start, b_start)
            hi = min(a_end, b_end)
            if lo <= hi:
                result.append([lo, hi])
            if a_end < b_end:
                i += 1
            else:
                j += 1
        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.intervalIntersection(
        [[0, 2], [5, 10], [13, 23], [24, 25]],
        [[1, 5], [8, 12], [15, 24], [25, 26]]
    )) 
    print(sol.intervalIntersection([[1, 3], [5, 9]], []))  
print(__name__)