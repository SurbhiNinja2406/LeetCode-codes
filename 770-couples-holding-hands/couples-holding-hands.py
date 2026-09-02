class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        n = len(row)
        pos = [0] * n
        for i, person in enumerate(row):
            pos[person] = i
        swaps = 0
        for i in range(0, n, 2):
            partner = row[i] ^ 1  
            if row[i + 1] != partner:
                partner_pos = pos[partner]
                other = row[i + 1]
                row[i + 1], row[partner_pos] = row[partner_pos], row[i + 1]
                pos[other] = partner_pos
                pos[partner] = i + 1
                swaps += 1
        return swaps
if __name__ == "__main__":
    sol = Solution()
    row = [0, 2, 1, 3]
    print("Input: row = {}".format(row))
    print("Output: {}".format(sol.minSwapsCouples(row)))
    print("Expected: 1\n")
    row = [3, 2, 0, 1]
    print("Input: row = {}".format(row))
    print("Output: {}".format(sol.minSwapsCouples(row)))
    print("Expected: 0\n")
print(__name__)