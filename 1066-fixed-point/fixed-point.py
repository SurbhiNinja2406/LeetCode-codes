class Solution(object):
    def fixedPoint(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if arr[mid] - mid >= 0:
                right = mid
            else:
                left = mid + 1
        if left < n and arr[left] == left:
            return left
        return -1
if __name__ == "__main__":
    sol = Solution()
    print(sol.fixedPoint([-10, -5, 0, 3, 7]))  
    print(sol.fixedPoint([0, 2, 5, 8, 17]))   
    print(sol.fixedPoint([-10, -5, 3, 4, 7, 9]))  
print(__name__)