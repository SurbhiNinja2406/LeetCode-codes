class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        revisions1 = version1.split('.')
        revisions2 = version2.split('.')
        max_len = max(len(revisions1), len(revisions2))
        for i in range(max_len):
            rev1 = int(revisions1[i]) if i < len(revisions1) else 0
            rev2 = int(revisions2[i]) if i < len(revisions2) else 0
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1
        return 0
if __name__ == "__main__":
    sol = Solution()
    print(sol.compareVersion("1.2", "1.10"))    
    print(sol.compareVersion("1.01", "1.001")) 
    print(sol.compareVersion("1.0", "1.0.0.0")) 
print(__name__)