class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}  
        max_length = 0
        left = 0 
        for right in range(len(s)):
            char = s[right]
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = right
            max_length = max(max_length, right - left + 1)
        return max_length
if __name__ == "__main__":
    sol = Solution()
    s = "abcabcbb"
    print(sol.lengthOfLongestSubstring(s))
    s = "bbbbb"
    print(sol.lengthOfLongestSubstring(s))
    s = "pwwkew"
    print(sol.lengthOfLongestSubstring(s))  
    s = ""
    print(sol.lengthOfLongestSubstring(s))  
    s = "a"
    print(sol.lengthOfLongestSubstring(s)) 
    s = "abcdef"
    print(sol.lengthOfLongestSubstring(s))  
print(__name__)