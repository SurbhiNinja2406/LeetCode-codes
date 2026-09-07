class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n < 3:
            return 0
        longest = 0
        i = 1
        while i < n - 1:
            if arr[i - 1] < arr[i] > arr[i + 1]:
                left = i - 1
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1
                right = i + 1
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1
                length = right - left + 1
                longest = max(longest, length)
                i = right
            else:
                i += 1
        return longest
if __name__ == "__main__":
    solution = Solution()
    arr1 = [2, 1, 4, 7, 3, 2, 5]
    print(solution.longestMountain(arr1))  
    arr2 = [2, 2, 2]
    print(solution.longestMountain(arr2)) 
    arr3 = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
    print(solution.longestMountain(arr3))  
    arr4 = [0, 1, 0, 2, 3, 4, 3, 2, 1, 0, 5, 6, 5]
    print(solution.longestMountain(arr4))  
    arr5 = [3, 2]
    print(solution.longestMountain(arr5))  
    arr6 = [1, 2, 2, 3, 1]
    print(solution.longestMountain(arr6))  
    arr7 = [5, 4, 3, 2, 1]
    print(solution.longestMountain(arr7)) 
print(__name__)