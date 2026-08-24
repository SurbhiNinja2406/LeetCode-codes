class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"        
        for _ in range(n - 1):
            result = self._runLengthEncode(result)        
        return result    
    def _runLengthEncode(self, s):
        encoded = []
        i = 0
        n = len(s)        
        while i < n:
            char = s[i]
            count = 1            
            while i + 1 < n and s[i + 1] == char:
                i += 1
                count += 1            
            encoded.append(str(count))
            encoded.append(char)
            i += 1        
        return "".join(encoded)
if __name__ == "__main__":
    solution = Solution()
    n1 = 4
    print(solution.countAndSay(n1)) 
    n2 = 1
    print(solution.countAndSay(n2))  
    for i in range(1, 7):
        print(i, "->", solution.countAndSay(i))
print(__name__)