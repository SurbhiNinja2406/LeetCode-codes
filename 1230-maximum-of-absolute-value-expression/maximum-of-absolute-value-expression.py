class Solution(object):
    def maxAbsValExpr(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        n = len(arr1)
        result = 0
        for s1 in (1, -1):
            for s2 in (1, -1):
                max_val = float('-inf')
                min_val = float('inf')
                for k in range(n):
                    v = s1 * arr1[k] + s2 * arr2[k] + k
                    if v > max_val:
                        max_val = v
                    if v < min_val:
                        min_val = v
                result = max(result, max_val - min_val)
        return result
if __name__ == "__main__":
    sol = Solution()
    arr1 = [1, 2, 3, 4]
    arr2 = [-1, 4, 5, 6]
    print(sol.maxAbsValExpr(arr1, arr2))  
    arr1 = [1, -2, -5, 0, 10]
    arr2 = [0, -2, -1, -7, -4]
    print(sol.maxAbsValExpr(arr1, arr2)) 
print(__name__)