class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)        
        if n <= 1:
            return 0
        is_palindrome = [[False] * n for _ in range(n)]
        for j in range(n):
            for i in range(j + 1):
                if s[i] == s[j] and (j - i <= 2 or is_palindrome[i + 1][j - 1]):
                    is_palindrome[i][j] = True
        min_cuts = [0] * n        
        for j in range(n):
            if is_palindrome[0][j]:
                min_cuts[j] = 0
            else:
                min_cuts[j] = float('inf')
                for i in range(1, j + 1):
                    if is_palindrome[i][j]:
                        min_cuts[j] = min(min_cuts[j], min_cuts[i - 1] + 1)        
        return min_cuts[n - 1]
if __name__ == "__main__":
    sol = Solution()
    s1 = "aab"
    print(sol.minCut(s1))  
    s2 = "a"
    print(sol.minCut(s2))  
    s3 = "ab"
    print(sol.minCut(s3)) 
print(__name__)