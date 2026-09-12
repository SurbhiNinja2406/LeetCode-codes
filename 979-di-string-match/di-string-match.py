class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        n = len(s)
        low, high = 0, n
        result = []
        for c in s:
            if c == 'I':
                result.append(low)
                low += 1
            else:  
                result.append(high)
                high -= 1
        result.append(low)
        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.diStringMatch("IDID"))  
    print(sol.diStringMatch("III"))  
    print(sol.diStringMatch("DDI"))  
print(__name__)