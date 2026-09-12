class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        if n < 3:
            return False
        i = 0
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        if i == 0 or i == n - 1:
            return False
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
        return i == n - 1
if __name__ == "__main__":
    sol = Solution()
    print(sol.validMountainArray([2, 1]))  
    print(sol.validMountainArray([3, 5, 5]))  
    print(sol.validMountainArray([0, 3, 2, 1]))  
    print(sol.validMountainArray([1, 2, 3, 4, 5])) 
    print(sol.validMountainArray([0, 2, 3, 4, 5, 2, 1, 0])) 
print(__name__)