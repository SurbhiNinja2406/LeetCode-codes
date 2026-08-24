class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        start, end = 0, 0
        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        for i in range(len(s)):
            len_odd = expand_from_center(i, i)     
            len_even = expand_from_center(i, i + 1) 
            max_len = max(len_odd, len_even)
            if max_len > end - start + 1:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start:end + 1]
if __name__ == "__main__":
    sol = Solution()
    s = "babad"
    print(sol.longestPalindrome(s))  
    s = "cbbd"
    print(sol.longestPalindrome(s)) 
    s = "a"
    print(sol.longestPalindrome(s)) 
    s = "racecar"
    print(sol.longestPalindrome(s)) 
    s = "abcde"
    print(sol.longestPalindrome(s)) 
    s = "aaaa"
    print(sol.longestPalindrome(s))  
    s = "bb"
    print(sol.longestPalindrome(s))  
print(__name__)