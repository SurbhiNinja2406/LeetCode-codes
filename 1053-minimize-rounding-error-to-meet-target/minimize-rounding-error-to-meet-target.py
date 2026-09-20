class Solution(object):
    def minimizeError(self, prices, target):
        """
        :type prices: List[str]
        :type target: int
        :rtype: str
        """
        floor_sum = 0
        fracs = []       
        floor_error = 0  
        for p in prices:
            whole, frac = p.split('.')
            whole = int(whole)
            frac = int(frac)
            floor_sum += whole
            if frac > 0:
                fracs.append(frac)
                floor_error += frac
        max_ceil = len(fracs)
        k = target - floor_sum
        if k < 0 or k > max_ceil:
            return "-1"
        fracs.sort(reverse=True)
        total_error = floor_error
        for i in range(k):
            total_error += 1000 - 2 * fracs[i]
        return "%d.%03d" % (total_error // 1000, total_error % 1000)
if __name__ == "__main__":
    sol = Solution()
    print(sol.minimizeError(["0.700", "2.800", "4.900"], 8)) 
    print(sol.minimizeError(["1.500", "2.500", "3.500"], 10)) 
    print(sol.minimizeError(["1.500", "2.500", "3.500"], 9))  
print(__name__)