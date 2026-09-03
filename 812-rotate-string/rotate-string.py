class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False
        return goal in (s + s)
if __name__ == "__main__":
    sol = Solution()
    print(sol.rotateString("abcde", "cdeab"))  
    print(sol.rotateString("abcde", "abced")) 
print(__name__)