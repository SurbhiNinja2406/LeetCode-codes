class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        result = []
        n = len(s)
        start = 0        
        for i in range(1, n + 1):
            if i == n or s[i] != s[start]:
                if i - start >= 3:
                    result.append([start, i - 1])
                start = i        
        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.largeGroupPositions("abbxxxxzzy"))     
    print(sol.largeGroupPositions("abc"))               
    print(sol.largeGroupPositions("abcdddeeeeaabbbcd"))   
print(__name__)