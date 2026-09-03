class Solution(object):
    def preimageSizeFZF(self, k):
        """
        :type k: int
        :rtype: int
        """
        def zeroes(x):
            count = 0
            power = 5
            while power <= x:
                count += x // power
                power *= 5
            return count
        lo, hi = 0, 5 * (k + 1) + 5  
        while lo < hi:
            mid = (lo + hi) // 2
            if zeroes(mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return 5 if zeroes(lo) == k else 0
if __name__ == "__main__":
    sol = Solution()
    print(sol.preimageSizeFZF(0))  
    print(sol.preimageSizeFZF(5)) 
    print(sol.preimageSizeFZF(3))  
print(__name__)