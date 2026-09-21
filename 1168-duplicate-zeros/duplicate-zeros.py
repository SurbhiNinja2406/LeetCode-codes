class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        zeros = arr.count(0)
        i = n - 1          
        j = n + zeros - 1   
        while i >= 0:
            if j < n:
                arr[j] = arr[i]
            if arr[i] == 0:
                j -= 1    
                if j < n:
                    arr[j] = 0
            i -= 1
            j -= 1
if __name__ == "__main__":
    sol = Solution()
    tests = [
        [1, 0, 2, 3, 0, 4, 5, 0],  
        [1, 2, 3],       
    ]
    for t in tests:
        original = list(t)
        sol.duplicateZeros(t)   
        print("arr = {} -> {}".format(original, t))
print(__name__)