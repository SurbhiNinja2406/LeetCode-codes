class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda iv: (iv[1], -iv[0]))
        p1, p2 = -1, -1
        count = 0
        for start, end in intervals:
            if p1 >= start and p2 >= start:
                continue
            elif p2 >= start:
                p1 = p2
                p2 = end
                count += 1
            else:
                p1 = end - 1
                p2 = end
                count += 2
        return count
if __name__ == "__main__":
    sol = Solution()
    print(sol.intersectionSizeTwo([[1, 3], [3, 7], [8, 9]]))
    print(sol.intersectionSizeTwo([[1, 3], [1, 4], [2, 5], [3, 5]]))
    print(sol.intersectionSizeTwo([[1, 2], [2, 3], [2, 4], [4, 5]]))
print(__name__)