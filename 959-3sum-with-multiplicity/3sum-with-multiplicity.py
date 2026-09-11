from collections import Counter
class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        MOD = 10**9 + 7
        count = Counter(arr)
        keys = sorted(count.keys())
        res = 0
        for i in range(len(keys)):
            x = keys[i]
            for j in range(i, len(keys)):
                y = keys[j]
                z = target - x - y
                if z < y:
                    break
                if z not in count:
                    continue
                if x == y == z:
                    res += count[x] * (count[x] - 1) * (count[x] - 2) // 6
                elif x == y:
                    res += count[x] * (count[x] - 1) // 2 * count[z]
                elif y == z:
                    res += count[x] * count[y] * (count[y] - 1) // 2
                else:
                    res += count[x] * count[y] * count[z]
        return res % MOD
if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSumMulti([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8))
    print(sol.threeSumMulti([1, 1, 2, 2, 2, 2], 5))
    print(sol.threeSumMulti([2, 1, 3], 6))
print(__name__)