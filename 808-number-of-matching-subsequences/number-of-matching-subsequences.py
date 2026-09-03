class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        from collections import defaultdict
        buckets = defaultdict(list)
        for word in words:
            buckets[word[0]].append((word, 0))
        count = 0
        for c in s:
            waiting = buckets[c]
            buckets[c] = [] 
            for word, idx in waiting:
                idx += 1
                if idx == len(word):
                    count += 1
                else:
                    buckets[word[idx]].append((word, idx))
        return count
if __name__ == "__main__":
    sol = Solution()
    print(sol.numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]))
    print(sol.numMatchingSubseq("dsahjpjauf", ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]))  
print(__name__)