class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n_cols = len(strs[0])
        n_rows = len(strs)
        count = 0
        for col in range(n_cols):
            for row in range(1, n_rows):
                if strs[row][col] < strs[row - 1][col]:
                    count += 1
                    break 
        return count
if __name__ == "__main__":
    sol = Solution()
    print(sol.minDeletionSize(["cba", "daf", "ghi"]))
    print(sol.minDeletionSize(["a", "b"])) 
    print(sol.minDeletionSize(["zyx", "wvu", "tsr"]))
print(__name__)