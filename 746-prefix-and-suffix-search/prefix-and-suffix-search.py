class WordFilter(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.weights = {}
        for index, word in enumerate(words):
            n = len(word)
            prefixes = [word[:i] for i in range(n + 1)]
            suffixes = [word[i:] for i in range(n + 1)]
            for p in prefixes:
                for s in suffixes:
                    key = p + "#" + s
                    self.weights[key] = index
    def f(self, pref, suff):
        """
        :type pref: str
        :type suff: str
        :rtype: int
        """
        return self.weights.get(pref + "#" + suff, -1)
if __name__ == "__main__":
    wordFilter = WordFilter(["apple"])
    result = wordFilter.f("a", "e")
    print("f('a', 'e') = {0}, Expected = 0".format(result))
    assert result == 0
    wordFilter2 = WordFilter(["apple"])
    result2 = wordFilter2.f("b", "e")
    print("f('b', 'e') = {0}, Expected = -1".format(result2))
    assert result2 == -1
    wordFilter3 = WordFilter(["apple", "apricot", "application"])
    result3 = wordFilter3.f("app", "n")
    print("f('app', 'n') = {0}, Expected = 2".format(result3))
    assert result3 == 2
    result4 = wordFilter3.f("ap", "cot")
    print("f('ap', 'cot') = {0}, Expected = 1".format(result4))
    assert result4 == 1
    print("\nAll test cases passed!")
print(__name__)
# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)