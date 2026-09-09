class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        alice_total = sum(aliceSizes)
        bob_total = sum(bobSizes)
        diff = (bob_total - alice_total) // 2
        bob_set = set(bobSizes)
        for a in aliceSizes:
            b = a + diff
            if b in bob_set:
                return [a, b]
        return []  
if __name__ == "__main__":
    sol = Solution()
    aliceSizes1, bobSizes1 = [1, 1], [2, 2]
    result1 = sol.fairCandySwap(aliceSizes1, bobSizes1)
    print("Example 1: {} (expected [1, 2])".format(result1))
    aliceSizes2, bobSizes2 = [1, 2], [2, 3]
    result2 = sol.fairCandySwap(aliceSizes2, bobSizes2)
    print("Example 2: {} (expected [1, 2])".format(result2))
    aliceSizes3, bobSizes3 = [2], [1, 3]
    result3 = sol.fairCandySwap(aliceSizes3, bobSizes3)
    print("Example 3: {} (expected [2, 3])".format(result3))
print(__name__)