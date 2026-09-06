class Solution(object):
    def uniqueLetterString(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        last = {chr(ord('A') + i): -1 for i in range(26)}
        prev_last = {chr(ord('A') + i): -1 for i in range(26)}        
        total = 0
        MOD = 2**31  
        for i, c in enumerate(s):
            total += (last[c] - prev_last[c]) * (i - last[c])
            prev_last[c] = last[c]
            last[c] = i
        for c in last:
            if last[c] != -1:
                total += (last[c] - prev_last[c]) * (n - last[c])        
        return total
if __name__ == "__main__":
    sol = Solution()
    print(sol.uniqueLetterString("ABC"))    
    print(sol.uniqueLetterString("ABA"))    
    print(sol.uniqueLetterString("LEETCODE"))  
print(__name__)