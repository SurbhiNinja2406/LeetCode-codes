class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        word_set = set(words)
        best = ""
        for word in words:
            can_build = True
            for i in range(1, len(word)):
                if word[:i] not in word_set:
                    can_build = False
                    break
            if can_build:
                if len(word) > len(best) or (len(word) == len(best) and word < best):
                    best = word
        return best
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestWord(["w", "wo", "wor", "worl", "world"]))
    print("Expected: world\n")
    print(sol.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))
    print("Expected: apple\n")
    print(repr(sol.longestWord(["ab", "abc"])))
    print("Expected: ''\n")
    print(sol.longestWord(["a", "b", "c"]))
    print("Expected: a (smallest lexicographically among length-1 words)\n")
    print(sol.longestWord(["a", "ab", "ac", "abc", "acb"]))
    print("Expected: abc (both abc and acb are length 3, abc < acb)")
print(__name__)