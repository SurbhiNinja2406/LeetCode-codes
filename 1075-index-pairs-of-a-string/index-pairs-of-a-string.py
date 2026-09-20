class Solution(object):
    def indexPairs(self, text, words):
        """
        :type text: str
        :type words: List[str]
        :rtype: List[List[int]]
        """
        word_set = set(words)
        max_len = max(len(w) for w in words)
        n = len(text)
        result = []
        for i in range(n):
            for j in range(i, min(n, i + max_len)):
                if text[i:j + 1] in word_set:
                    result.append([i, j])
        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.indexPairs("thestoryofleetcodeandme",
                         ["story", "fleet", "leetcode"])) 
    print(sol.indexPairs("ababa", ["aba", "ab"]))        
print(__name__)