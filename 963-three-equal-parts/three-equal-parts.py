class Solution(object):
    def threeEqualParts(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        ones = [i for i, v in enumerate(arr) if v == 1]
        total_ones = len(ones)
        if total_ones % 3 != 0:
            return [-1, -1]
        if total_ones == 0:
            return [0, n - 1]
        k = total_ones // 3  
        i1, j1 = ones[0], ones[k - 1]
        i2, j2 = ones[k], ones[2 * k - 1]
        i3, j3 = ones[2 * k], ones[3 * k - 1]
        length = n - i3
        if (j1 - i1 + 1) > length or (j2 - i2 + 1) > length:
            return [-1, -1]
        part1 = arr[i1:i1 + length]
        part2 = arr[i2:i2 + length]
        part3 = arr[i3:i3 + length]
        if part1 == part2 == part3:
            return [i1 + length - 1, i2 + length]
        return [-1, -1]
if __name__ == "__main__":
    sol = Solution()
    print(sol.threeEqualParts([1, 0, 1, 0, 1]))
    print(sol.threeEqualParts([1, 1, 0, 1, 1]))
    print(sol.threeEqualParts([1, 1, 0, 0, 1]))