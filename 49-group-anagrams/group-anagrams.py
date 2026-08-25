class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}        
        for s in strs:
            key = "".join(sorted(s))
            if key not in groups:
                groups[key] = []            
            groups[key].append(s)        
        return list(groups.values())
if __name__ == "__main__":
    solution = Solution()
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams(strs1))
    strs2 = [""]
    print(solution.groupAnagrams(strs2))
    strs3 = ["a"]
    print(solution.groupAnagrams(strs3))
print(__name__)