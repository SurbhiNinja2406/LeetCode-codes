class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev_run = 0   
        curr_run = 1   
        result = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr_run += 1
            else:
                result += min(prev_run, curr_run)
                prev_run = curr_run
                curr_run = 1
        result += min(prev_run, curr_run)
        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.countBinarySubstrings("00110011")) 
    print(sol.countBinarySubstrings("10101"))     
print(__name__)