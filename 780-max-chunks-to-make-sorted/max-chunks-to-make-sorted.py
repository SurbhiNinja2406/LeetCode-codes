class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        chunks = 0
        max_so_far = 0
        for i, num in enumerate(arr):
            max_so_far = max(max_so_far, num)
            if max_so_far == i:
                chunks += 1
        return chunks
if __name__ == "__main__":
    sol = Solution()
    arr = [4, 3, 2, 1, 0]
    print("Input: arr = {}".format(arr))
    print("Output: {}".format(sol.maxChunksToSorted(arr)))
    print("Expected: 1\n")
    arr = [1, 0, 2, 3, 4]
    print("Input: arr = {}".format(arr))
    print("Output: {}".format(sol.maxChunksToSorted(arr)))
    print("Expected: 4\n")
print(__name__)