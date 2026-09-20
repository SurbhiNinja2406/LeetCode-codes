class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        m = len(target)
        j = 0       
        count = 0  
        while j < m:
            start = j
            for ch in source:
                if j < m and ch == target[j]:
                    j += 1
            if j == start:
                return -1
            count += 1
        return count
if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestWay("abc", "abcbc"))   
    print(sol.shortestWay("abc", "acdbc"))  
    print(sol.shortestWay("xyz", "xzyxz"))  
print(__name__)