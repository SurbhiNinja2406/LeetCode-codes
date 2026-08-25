class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_count = {}  
        left = 0         
        max_len = 0
        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            while len(char_count) > 2:
                left_char = s[left]
                char_count[left_char] -= 1
                if char_count[left_char] == 0:
                    del char_count[left_char]
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
if __name__ == "__main__":
    obj = Solution()
    s1 = "eceba"
    print(obj.lengthOfLongestSubstringTwoDistinct(s1)) 
    s2 = "ccaabbb"
    print(obj.lengthOfLongestSubstringTwoDistinct(s2))  
    s3 = "a"
    print(obj.lengthOfLongestSubstringTwoDistinct(s3))  
    s4 = "aaaa"
    print(obj.lengthOfLongestSubstringTwoDistinct(s4))  
    s5 = "abcdef"
    print(obj.lengthOfLongestSubstringTwoDistinct(s5)) 