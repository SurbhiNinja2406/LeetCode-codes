class Solution(object):
    def areSentencesSimilarTwo(self, sentence1, sentence2, similarPairs):
        """
        :type sentence1: List[str]
        :type sentence2: List[str]
        :type similarPairs: List[List[str]]
        :rtype: bool
        """
        if len(sentence1) != len(sentence2):
            return False
        parent = {}
        def find(x):
            if x not in parent:
                parent[x] = x
            while parent[x] != x:
                parent[x] = parent[parent[x]]  
                x = parent[x]
            return x
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry
        for x, y in similarPairs:
            union(x, y)
        for w1, w2 in zip(sentence1, sentence2):
            if w1 == w2:
                continue  
            if w1 not in parent or w2 not in parent:
                return False
            if find(w1) != find(w2):
                return False
        return True
if __name__ == "__main__":
    sol = Solution()
    sentence1 = ["great", "acting", "skills"]
    sentence2 = ["fine", "drama", "talent"]
    similarPairs = [["great", "good"], ["fine", "good"], ["drama", "acting"], ["skills", "talent"]]
    print(sol.areSentencesSimilarTwo(sentence1, sentence2, similarPairs))
    sentence1 = ["I", "love", "leetcode"]
    sentence2 = ["I", "love", "onepiece"]
    similarPairs = [["manga", "onepiece"], ["platform", "anime"], ["leetcode", "platform"], ["anime", "manga"]]
    print(sol.areSentencesSimilarTwo(sentence1, sentence2, similarPairs))
    sentence1 = ["I", "love", "leetcode"]
    sentence2 = ["I", "love", "onepiece"]
    similarPairs = [["manga", "hunterXhunter"], ["platform", "anime"], ["leetcode", "platform"], ["anime", "manga"]]
    print(sol.areSentencesSimilarTwo(sentence1, sentence2, similarPairs))
print(__name__)