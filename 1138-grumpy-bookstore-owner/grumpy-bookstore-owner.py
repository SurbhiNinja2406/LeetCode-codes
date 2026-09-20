class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        n = len(customers)
        base = 0
        for i in range(n):
            if grumpy[i] == 0:
                base += customers[i]
        extra = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                extra += customers[i]
        max_extra = extra
        for i in range(minutes, n):
            if grumpy[i] == 1:
                extra += customers[i]
            if grumpy[i - minutes] == 1:
                extra -= customers[i - minutes]
            max_extra = max(max_extra, extra)
        return base + max_extra
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5],
                           [0, 1, 0, 1, 0, 1, 0, 1], 3))
    print(sol.maxSatisfied([1], [0], 1))                