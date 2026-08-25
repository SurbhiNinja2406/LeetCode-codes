class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        length = 0
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1        
        return length
if __name__ == "__main__":
    solution = Solution()
    s1 = "Hello World"
    print(solution.lengthOfLastWord(s1)) 
    s2 = "   fly me   to   the moon  "
    print(solution.lengthOfLastWord(s2))  
    s3 = "luffy is still joyboy"
    print(solution.lengthOfLastWord(s3))  
print(__name__)