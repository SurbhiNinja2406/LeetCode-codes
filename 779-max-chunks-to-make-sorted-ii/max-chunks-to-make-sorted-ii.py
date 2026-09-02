class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n == 0:
            return 0
        suffix_min = [0] * n
        suffix_min[-1] = arr[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(arr[i], suffix_min[i + 1])
        chunks = 0
        prefix_max = float('-inf')
        for i in range(n):
            prefix_max = max(prefix_max, arr[i])
            if i == n - 1 or prefix_max <= suffix_min[i + 1]:
                chunks += 1
        return chunks
if __name__ == "__main__":
    sol = Solution()
    arr = [5, 4, 3, 2, 1]
    print("Input: arr = {}".format(arr))
    print("Output: {}".format(sol.maxChunksToSorted(arr)))
    print("Expected: 1\n")
    arr = [2, 1, 3, 4, 4]
    print("Input: arr = {}".format(arr))
    print("Output: {}".format(sol.maxChunksToSorted(arr)))
    print("Expected: 4\n")
print(__name__)