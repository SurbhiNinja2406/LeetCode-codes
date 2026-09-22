# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        n = mountain_arr.length()
        peak = self._find_peak(mountain_arr, n)
        left_result = self._binary_search(mountain_arr, target, 0, peak, ascending=True)
        if left_result != -1:
            return left_result
        right_result = self._binary_search(mountain_arr, target, peak + 1, n - 1, ascending=False)
        return right_result    
    def _find_peak(self, mountain_arr, n):
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                lo = mid + 1
            else:
                hi = mid
        return lo    
    def _binary_search(self, mountain_arr, target, lo, hi, ascending):
        while lo <= hi:
            mid = (lo + hi) // 2
            val = mountain_arr.get(mid)            
            if val == target:
                return mid            
            if ascending:
                if val < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                if val > target:
                    lo = mid + 1
                else:
                    hi = mid - 1        
        return -1
class MountainArray(object):
    def __init__(self, arr):
        self.arr = arr
        self.call_count = 0
    def get(self, index):
        self.call_count += 1
        if self.call_count > 100:
            raise Exception("Too many calls to MountainArray.get()")
        return self.arr[index]
    def length(self):
        return len(self.arr)
if __name__ == "__main__":
    solution = Solution()
    arr1 = [1, 2, 3, 4, 5, 3, 1]
    mountain1 = MountainArray(arr1)
    result1 = solution.findInMountainArray(3, mountain1)
    print("Example 1: {} (Expected: 2)".format(result1))
    print("  get() calls used: {}".format(mountain1.call_count))
    arr2 = [0, 1, 2, 4, 2, 1]
    mountain2 = MountainArray(arr2)
    result2 = solution.findInMountainArray(3, mountain2)
    print("Example 2: {} (Expected: -1)".format(result2))
    print("  get() calls used: {}".format(mountain2.call_count))
print(__name__)