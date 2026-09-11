class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i, j = 0, 0
        n, m = len(name), len(typed)
        while j < m:
            if i < n and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
        return i == n
if __name__ == "__main__":
    sol = Solution()
    print(sol.isLongPressedName("alex", "aaleex"))
    print(sol.isLongPressedName("saeed", "ssaaedd"))
print(__name__)