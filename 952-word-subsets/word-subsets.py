from collections import Counter
class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        max_req = Counter()
        for w in words2:
            c = Counter(w)
            for ch, cnt in c.items():
                if cnt > max_req[ch]:
                    max_req[ch] = cnt
        result = []
        for w in words1:
            c = Counter(w)
            if all(c[ch] >= cnt for ch, cnt in max_req.items()):
                result.append(w)
        return result
if __name__ == "__main__":
    sol = Solution()
    words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
    words2 = ["e", "o"]
    print(sol.wordSubsets(words1, words2))
    words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
    words2 = ["lc", "eo"]
    print(sol.wordSubsets(words1, words2))
    words1 = ["acaac", "cccbb", "aacbb", "caacc", "bcbbb"]
    words2 = ["c", "cc", "b"]
    print(sol.wordSubsets(words1, words2))
print(__name__)