class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        memo = {}
        def helper(s1, s2):
            if (s1, s2) in memo:
                return memo[(s1, s2)]
            if s1 == s2:
                memo[(s1, s2)] = True
                return True
            if len(s1) != len(s2) or sorted(s1) != sorted(s2):
                memo[(s1, s2)] = False
                return False
            n = len(s1)
            for i in range(1, n):
                if helper(s1[:i], s2[:i]) and helper(s1[i:], s2[i:]):
                    memo[(s1, s2)] = True
                    return True
                if helper(s1[:i], s2[n - i:]) and helper(s1[i:], s2[:n - i]):
                    memo[(s1, s2)] = True
                    return True
            memo[(s1, s2)] = False
            return False
        return helper(s1, s2)
if __name__ == "__main__":
    sol = Solution()
    print(sol.isScramble("great", "rgeat")) 
    print(sol.isScramble("abcde", "caebd"))  
    print(sol.isScramble("a", "a"))    
print(__name__)