class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n == 1:
            return 1
        max_len = 1
        up = 1
        down = 1
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                up = down + 1
                down = 1
            elif arr[i] < arr[i - 1]:
                down = up + 1
                up = 1
            else:
                up = 1
                down = 1
            max_len = max(max_len, up, down)
        return max_len
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))  
    print(sol.maxTurbulenceSize([4, 8, 12, 16]))             
    print(sol.maxTurbulenceSize([100]))                 
print(__name__)