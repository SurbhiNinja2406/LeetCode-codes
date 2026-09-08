class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        index_map = {val: i for i, val in enumerate(arr)}
        dp = {}        
        max_length = 0
        for j in range(n):
            for i in range(j):
                prev_val = arr[j] - arr[i]
                if prev_val < arr[i] and prev_val in index_map:
                    k = index_map[prev_val]
                    dp[(i, j)] = dp.get((k, i), 2) + 1
                    max_length = max(max_length, dp[(i, j)])        
        return max_length if max_length >= 3 else 0
if __name__ == "__main__":
    sol = Solution()
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
    result1 = sol.lenLongestFibSubseq(arr1)
    print("Example 1:")
    print("Input: arr = {}".format(arr1))
    print("Output:", result1)
    print("Expected: 5")
    print()
    arr2 = [1, 3, 7, 11, 12, 14, 18]
    result2 = sol.lenLongestFibSubseq(arr2)
    print("Example 2:")
    print("Input: arr = {}".format(arr2))
    print("Output:", result2)
    print("Expected: 3")
    print()
    arr3 = [1, 2, 4, 8, 16, 32]
    result3 = sol.lenLongestFibSubseq(arr3)
    print("Additional test (no valid subsequence):")
    print("Input: arr = {}".format(arr3))
    print("Output:", result3)
    print("Expected: 0")
    print()
    arr4 = [1, 2, 3, 5, 8, 13, 21]
    result4 = sol.lenLongestFibSubseq(arr4)
    print("Additional test (entire array is Fibonacci):")
    print("Input: arr = {}".format(arr4))
    print("Output:", result4)
    print("Expected: 7")
print(__name__)