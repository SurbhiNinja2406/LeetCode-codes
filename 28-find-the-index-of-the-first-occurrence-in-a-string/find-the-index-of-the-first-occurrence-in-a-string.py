class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n, m = len(haystack), len(needle)
        for start in range(n - m + 1):
            if haystack[start:start + m] == needle:
                return start
        return -1
if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("sadbutsad", "sad")) 
    print(sol.strStr("leetcode", "leeto"))
    print(sol.strStr("abc", "abc"))  
    print(sol.strStr("hello", "l")) 
    print(sol.strStr("mississippi", "issip")) 
    print(sol.strStr("ab", "abc")) 
    print(sol.strStr("aaaaa", "bba")) 
    print(sol.strStr("abcabc", "abc"))  
print(__name__)