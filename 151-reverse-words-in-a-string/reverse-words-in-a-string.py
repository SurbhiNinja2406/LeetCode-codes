class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        return ' '.join(reversed(words))
if __name__ == "__main__":
    sol = Solution()
    s1 = "the sky is blue"
    print(sol.reverseWords(s1)) 
    s2 = "  hello world  "
    print(sol.reverseWords(s2))  
    s3 = "a good   example"
    print(sol.reverseWords(s3))  
print(__name__)