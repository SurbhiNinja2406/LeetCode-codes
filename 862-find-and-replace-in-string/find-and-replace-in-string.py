class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        """
        :type s: str
        :type indices: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        n = len(s)
        from collections import defaultdict
        by_index = defaultdict(list)
        for idx, src, tgt in zip(indices, sources, targets):
            by_index[idx].append((src, tgt))        
        result = []
        i = 0        
        while i < n:
            matched = False
            if i in by_index:
                for source, target in by_index[i]:
                    if s[i:i + len(source)] == source:
                        result.append(target)
                        i += len(source)
                        matched = True
                        break
            if not matched:
                result.append(s[i])
                i += 1        
        return ''.join(result)
if __name__ == "__main__":
    sol = Solution()
    print(sol.findReplaceString("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"]))  
    print(sol.findReplaceString("abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"])) 
    print(sol.findReplaceString("abcde", [2, 2], ["bc", "cde"], ["fe", "f"]))
print(__name__)