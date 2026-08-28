from collections import Counter

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counts = Counter(words)
        sorted_words = sorted(counts.keys(), key=lambda w: (-counts[w], w))
        return sorted_words[:k]
if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
    print(sol.topKFrequent(
        ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
print(__name__)