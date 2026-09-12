from itertools import permutations
class Solution(object):
    def largestTimeFromDigits(self, arr):
        """
        :type arr: List[int]
        :rtype: str
        """
        best = -1
        best_time = ""
        for perm in permutations(arr):
            h1, h2, m1, m2 = perm
            hour = h1 * 10 + h2
            minute = m1 * 10 + m2
            if hour < 24 and minute < 60:
                total_minutes = hour * 60 + minute
                if total_minutes > best:
                    best = total_minutes
                    best_time = "{:02d}:{:02d}".format(hour, minute)
        return best_time
if __name__ == "__main__":
    sol = Solution()
    print(sol.largestTimeFromDigits([1, 2, 3, 4])) 
    print(sol.largestTimeFromDigits([5, 5, 5, 5]))  
print(__name__)