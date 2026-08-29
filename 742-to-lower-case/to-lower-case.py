class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for ch in s:
            code = ord(ch)
            if 65 <= code <= 90:   # 'A' to 'Z'
                result.append(chr(code + 32))
            else:
                result.append(ch)
        return "".join(result)
if __name__ == "__main__":
    sol = Solution()
    print(sol.toLowerCase("Hello"))  
    print(sol.toLowerCase("here"))   
    print(sol.toLowerCase("LOVELY"))  
print(__name__)