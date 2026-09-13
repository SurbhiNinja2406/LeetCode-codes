class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n = len(strs)        
        m = len(strs[0])    
        dp = [1] * m
        
        for j in range(m):
            for k in range(j):
                valid = True
                for i in range(n):
                    if strs[i][k] > strs[i][j]:
                        valid = False
                        break                
                if valid:
                    dp[j] = max(dp[j], dp[k] + 1)        
        longest_valid = max(dp) if dp else 0
        return m - longest_valid
if __name__ == "__main__":
    sol = Solution()
    strs1 = ["babca", "bbazb"]
    result1 = sol.minDeletionSize(strs1)
    print("Input: {}".format(strs1))
    print("Output: {}".format(result1))
    print("Expected: 3")
    print("Pass: {}\n".format(result1 == 3))
    strs2 = ["edcba"]
    result2 = sol.minDeletionSize(strs2)
    print("Input: {}".format(strs2))
    print("Output: {}".format(result2))
    print("Expected: 4")
    print("Pass: {}\n".format(result2 == 4))
    strs3 = ["ghi", "def", "abc"]
    result3 = sol.minDeletionSize(strs3)
    print("Input: {}".format(strs3))
    print("Output: {}".format(result3))
    print("Expected: 0")
    print("Pass: {}\n".format(result3 == 0))
    strs4 = ["abc"]
    result4 = sol.minDeletionSize(strs4)
    print("Input: {}".format(strs4))
    print("Output: {}".format(result4))
    print("Expected: 0")
    print("Pass: {}\n".format(result4 == 0))
    strs5 = ["a", "b", "c"]
    result5 = sol.minDeletionSize(strs5)
    print("Input: {}".format(strs5))
    print("Output: {}".format(result5))
    print("Expected: 0")
    print("Pass: {}\n".format(result5 == 0))
    strs6 = ["cba", "cba", "cba"]
    result6 = sol.minDeletionSize(strs6)
    print("Input: {}".format(strs6))
    print("Output: {}".format(result6))
    print("Expected: 2")
    print("Pass: {}\n".format(result6 == 2)) 
print(__name__)