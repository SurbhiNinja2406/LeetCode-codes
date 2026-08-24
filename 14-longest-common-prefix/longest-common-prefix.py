class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["flower", "flow", "flight"])) 
    print(sol.longestCommonPrefix(["dog", "racecar", "car"])) 
    print(sol.longestCommonPrefix(["single"]))
    print(sol.longestCommonPrefix(["test", "test", "test"])) 
    print(sol.longestCommonPrefix(["a", "ab", "abc"])) 
    print(sol.longestCommonPrefix(["", "b", "c"]))  
    print(sol.longestCommonPrefix(["abc", "xyz"])) 
    print(sol.longestCommonPrefix(["a", "a", "a"])) 
print(__name__)