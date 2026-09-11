class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        ones_count = 0   
        flips = 0   
        for ch in s:
            if ch == '1':
                ones_count += 1
            else:
                flips = min(flips + 1, ones_count)
        return flips
if __name__ == "__main__":
    sol = Solution()
    print(sol.minFlipsMonoIncr("00110"))
    print(sol.minFlipsMonoIncr("010110"))
    print(sol.minFlipsMonoIncr("00011000"))
print(__name__)