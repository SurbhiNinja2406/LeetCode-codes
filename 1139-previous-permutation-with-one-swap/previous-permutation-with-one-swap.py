class Solution(object):
    def prevPermOpt1(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        i = n - 2
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1
        if i < 0:
            return arr
        j = n - 1
        while arr[j] >= arr[i]:
            j -= 1
        while arr[j - 1] == arr[j]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
        return arr
if __name__ == "__main__":
    sol = Solution()
    print(sol.prevPermOpt1([3, 2, 1]))    
    print(sol.prevPermOpt1([1, 1, 5]))  
    print(sol.prevPermOpt1([1, 9, 4, 6, 7])) 
    print(sol.prevPermOpt1([3, 1, 1, 3]))  
print(__name__)