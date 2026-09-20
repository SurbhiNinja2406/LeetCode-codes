from collections import Counter
class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        n = len(barcodes)
        count = Counter(barcodes)
        ordered = sorted(barcodes, key=lambda x: (-count[x], x))
        result = [0] * n
        half = (n + 1) // 2
        result[0::2] = ordered[:half]
        result[1::2] = ordered[half:]
        return result
if __name__ == "__main__":
    sol = Solution()
    def is_valid(arr):
        return all(arr[i] != arr[i + 1] for i in range(len(arr) - 1))
    tests = [
        [1, 1, 1, 2, 2, 2],
        [1, 1, 1, 1, 2, 2, 3, 3],
        [1, 1, 2, 2, 3],
    ]
    for t in tests:
        res = sol.rearrangeBarcodes(t)
        print(res, "valid" if is_valid(res) else "INVALID")
print(__name__)