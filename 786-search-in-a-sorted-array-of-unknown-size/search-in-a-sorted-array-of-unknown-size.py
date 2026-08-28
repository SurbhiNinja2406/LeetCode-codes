# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
class ArrayReader(object):
    def __init__(self, arr):
        self.arr = arr
    def get(self, index):
        if index < 0 or index >= len(self.arr):
            return 2**31 - 1
        return self.arr[index]
class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        OUT_OF_BOUNDS = 2**31 - 1
        if reader.get(0) == target:
            return 0
        lo, hi = 0, 1
        while reader.get(hi) < target:
            lo = hi
            hi *= 2
            if reader.get(hi) == OUT_OF_BOUNDS:
                break
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            val = reader.get(mid)
            if val == target:
                return mid
            elif val > target:  
                hi = mid - 1
            else:
                lo = mid + 1
        return -1
if __name__ == "__main__":
    sol = Solution()
    reader1 = ArrayReader([-1, 0, 3, 5, 9, 12])
    print(sol.search(reader1, 9))   
    reader2 = ArrayReader([-1, 0, 3, 5, 9, 12])
    print(sol.search(reader2, 2))   
print(__name__)