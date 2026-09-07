class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
if __name__ == "__main__":
    solution = Solution()
    arr1 = [0, 1, 0]
    print(solution.peakIndexInMountainArray(arr1))  
    arr2 = [0, 2, 1, 0]
    print(solution.peakIndexInMountainArray(arr2))  
    arr3 = [0, 10, 5, 2]
    print(solution.peakIndexInMountainArray(arr3)) 
    arr4 = [0, 1, 2, 3, 4, 5, 4, 3]
    print(solution.peakIndexInMountainArray(arr4))  
    arr5 = [0, 5, 4, 3, 2, 1]
    print(solution.peakIndexInMountainArray(arr5))  
    arr6 = [1, 3, 5, 7, 9, 11, 8, 4, 2]
    print(solution.peakIndexInMountainArray(arr6))  