class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2, similarPairs):
        """
        :type sentence1: List[str]
        :type sentence2: List[str]
        :type similarPairs: List[List[str]]
        :rtype: bool
        """
        if len(sentence1) != len(sentence2):
            return False
        similar_set = set()
        for x, y in similarPairs:
            similar_set.add((x, y))
            similar_set.add((y, x))
        for w1, w2 in zip(sentence1, sentence2):
            if w1 == w2:
                continue
            if (w1, w2) not in similar_set:
                return False
        return True
if __name__ == "__main__":
    sol = Solution()
    sentence1 = ["great", "acting", "skills"]
    sentence2 = ["fine", "drama", "talent"]
    similarPairs = [["great", "fine"], ["drama", "acting"], ["skills", "talent"]]
    print(sol.areSentencesSimilar(sentence1, sentence2, similarPairs))
    sentence1 = ["great"]
    sentence2 = ["great"]
    similarPairs = []
    print(sol.areSentencesSimilar(sentence1, sentence2, similarPairs))
    sentence1 = ["great"]
    sentence2 = ["doubleplus", "good"]
    similarPairs = [["great", "doubleplus"]]
    print(sol.areSentencesSimilar(sentence1, sentence2, similarPairs))
print(__name__)